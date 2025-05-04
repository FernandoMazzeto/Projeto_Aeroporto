from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

class SessaoCreate(BaseModel):
    email: EmailStr
    senha: str
    ip: str

    @field_validator('senha')
    def validar_senha(cls, v):
        if len(v) < 8:
            raise ValueError("Senha deve ter pelo menos 8 caracteres")
        return v

class SessaoResponse(BaseModel):
    chave: str
    expira_em: datetime  

class SessaoValida(BaseModel):
    chave: str