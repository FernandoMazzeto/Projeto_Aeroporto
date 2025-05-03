from pydantic import BaseModel
from datetime import datetime

class CompraCreate(BaseModel):
    voo_id: int
    chave: str  # chave da sessão

class CompraResponse(BaseModel):
    id: int
    usuario_id: int
    voo_id: int
    data_compra: datetime

    class Config:
        orm_mode = True