from pydantic import BaseModel

class AeroportoResponse(BaseModel):
    id: int
    sigla: str
    nome: str
    cidade: str
    estado: str

    class Config:
        orm_mode = True