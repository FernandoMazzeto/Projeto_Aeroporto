from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Voo(Base):
    __tablename__ = "voos"

    id = Column(Integer, primary_key=True, index=True)
    origem_id = Column(Integer, ForeignKey("aeroportos.id"), nullable=False)
    destino_id = Column(Integer, ForeignKey("aeroportos.id"), nullable=False)
    data_partida = Column(DateTime, nullable=False)
    duracao = Column(String, nullable=False)  # Ex: "2h30min"
    companhia = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)  # em centavos ou reais

    origem = relationship("Aeroporto", foreign_keys=[origem_id])
    destino = relationship("Aeroporto", foreign_keys=[destino_id])
