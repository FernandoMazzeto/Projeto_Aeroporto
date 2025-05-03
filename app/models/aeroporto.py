from sqlalchemy import Column, Integer, String
from app.database import Base

class Aeroporto(Base):
    __tablename__ = "aeroportos"

    id = Column(Integer, primary_key=True, index=True)
    sigla = Column(String(3), unique=True, nullable=False)  # Ex: GRU, GIG
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String(2), nullable=False)