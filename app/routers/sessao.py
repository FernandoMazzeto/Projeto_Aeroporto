from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.models.sessao import Sessao
from app.schemas.sessao import SessaoCreate, SessaoResponse, SessaoValida
from passlib.context import CryptContext
import uuid
from datetime import datetime, timedelta

# Configurações
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
TEMPO_EXPIRACAO_MINUTOS = 20  # Tempo de expiração reduzido para 20 minutos

router = APIRouter(prefix="/sessao", tags=["Sessão"])

@router.post("/login", response_model=SessaoResponse)
def login(dados: SessaoCreate, db: Session = Depends(get_db)):
    # Verifica credenciais
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    
    if not usuario or not pwd_context.verify(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Cria nova sessão com tempo de expiração controlado
    chave = str(uuid.uuid4())
    data_atual = datetime.utcnow()
    sessao = Sessao(
        chave=chave,
        usuario_id=usuario.id,
        ip=dados.ip,
        criada_em=data_atual,
        expira_em=data_atual + timedelta(minutes=TEMPO_EXPIRACAO_MINUTOS),
        ativa=True
    )
    
    db.add(sessao)
    db.commit()
    db.refresh(sessao)
    
    return SessaoResponse(
        chave=sessao.chave, 
        expira_em=sessao.expira_em,
        mensagem=f"Sessão válida por {TEMPO_EXPIRACAO_MINUTOS} minutos"
    )

@router.post("/logout")
def logout(dados: SessaoValida, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(
        Sessao.chave == dados.chave,
        Sessao.ativa == True,
        Sessao.expira_em > datetime.utcnow()
    ).first()
    
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessão não encontrada ou expirada")
    
    sessao.ativa = False
    sessao.expira_em = datetime.utcnow()  # Força expiração imediata
    db.commit()
    return {"mensagem": "Logout realizado com sucesso"}

@router.post("/validar")
def validar_sessao(dados: SessaoValida, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(
        Sessao.chave == dados.chave,
        Sessao.ativa == True,
        Sessao.expira_em > datetime.utcnow()
    ).first()
    
    if not sessao:
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")
    
    # Calcula tempo restante
    tempo_restante = sessao.expira_em - datetime.utcnow()
    minutos_restantes = round(tempo_restante.total_seconds() / 60)
    
    return {
        "valida": True,
        "usuario_id": sessao.usuario_id,
        "tempo_restante_minutos": minutos_restantes,
        "expira_em": sessao.expira_em.isoformat()
    }