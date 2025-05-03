# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# Criação da engine, sessão e base
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Importar os modelos aqui para garantir que o SQLAlchemy registre todas as tabelas
def criar_tabelas():
    from app.models import usuario, sessao, aeroporto, voo, compra  # <-- Importa todos os modelos!
    Base.metadata.create_all(bind=engine)

# Dependency para injetar a sessão do banco nos endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
