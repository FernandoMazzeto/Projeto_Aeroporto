from pydantic import BaseModel
from datetime import datetime
from typing import List

class CompraCreate(BaseModel):
    voo_id: int
    passageiros: int  
    chave: str  

class CompraResponse(BaseModel):
    id: int
    localizador: str  
    tickets: List[str]  
    usuario_id: int
    voo_id: int
    data_compra: datetime

    class Config:
        orm_mode = True