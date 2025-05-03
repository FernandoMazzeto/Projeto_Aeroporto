from pydantic import BaseModel
from datetime import datetime

class VooResponse(BaseModel):
    id: int
    origem_id: int
    destino_id: int
    data_partida: datetime
    duracao: str
    companhia: str
    preco: int

    class Config:
        orm_mode = True