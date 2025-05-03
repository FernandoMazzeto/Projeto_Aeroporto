from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.models.sessao import Sessao
from app.schemas.sessao import SessaoCreate, SessaoResponse, SessaoValida
import uuid

router = APIRouter(prefix="/sessao", tags=["Sessão"])

@router.post("/login", response_model=SessaoResponse)
def login(dados: SessaoCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email, Usuario.senha == dados.senha).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    chave = str(uuid.uuid4())
    sessao = Sessao(chave=chave, usuario_id=usuario.id, ip=dados.ip)
    db.add(sessao)
    db.commit()
    db.refresh(sessao)
    return SessaoResponse(chave=sessao.chave)

@router.post("/logout")
def logout(dados: SessaoValida, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(Sessao.chave == dados.chave, Sessao.ativa == "S").first()
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    
    sessao.ativa = "N"
    db.commit()
    return {"mensagem": "Logout realizado com sucesso"}

@router.post("/validar")
def validar_sessao(dados: SessaoValida, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(Sessao.chave == dados.chave, Sessao.ativa == "S").first()
    if not sessao:
        raise HTTPException(status_code=401, detail="Sessão inválida")
    
    return {"valida": True}