from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    voo_id = Column(Integer, ForeignKey("voos.id"), nullable=False)
    data_compra = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario")
    voo = relationship("Voo")