from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True