from pydantic import BaseModel, EmailStr, field_validator

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

    @field_validator('senha')
    def validar_senha(cls, v):
        if len(v) < 8:
            raise ValueError("Senha deve ter no mínimo 8 caracteres")
        if not any(c.isupper() for c in v):
            raise ValueError("Senha deve conter pelo menos 1 letra maiúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("Senha deve conter pelo menos 1 número")
        return v

class UsuarioResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True