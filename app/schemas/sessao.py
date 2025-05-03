from pydantic import BaseModel

class SessaoCreate(BaseModel):
    email: str
    senha: str
    ip: str

class SessaoResponse(BaseModel):
    chave: str

class SessaoValida(BaseModel):
    chave: str