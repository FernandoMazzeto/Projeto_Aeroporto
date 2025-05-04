from sqlalchemy import Column, Integer, String
from app.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)  # Armazenará o hash

    def set_senha(self, senha_plana: str):
        """Gera e armazena o hash da senha"""
        self.senha = pwd_context.hash(senha_plana)

    def verificar_senha(self, senha_plana: str) -> bool:
        """Verifica se a senha está correta"""
        return pwd_context.verify(senha_plana, self.senha)