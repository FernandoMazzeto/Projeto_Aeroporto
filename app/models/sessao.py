from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from app.database import Base

class Sessao(Base):
    __tablename__ = "sessoes"

    id = Column(Integer, primary_key=True, index=True)
    chave = Column(String, unique=True, index=True, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ip = Column(String, nullable=False)
    criada_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime, nullable=False)  
    ativa = Column(Boolean, default=True)

    usuario = relationship("Usuario")