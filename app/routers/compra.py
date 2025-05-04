from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.compra import Compra
from app.models.sessao import Sessao
from app.schemas.compra import CompraCreate, CompraResponse
from datetime import datetime
from uuid import uuid4

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.post("/", response_model=CompraResponse)
def comprar_passagem(dados: CompraCreate, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(
        Sessao.chave == dados.chave,
        Sessao.ativa == True,
        Sessao.expira_em > datetime.utcnow()
    ).first()
    
    if not sessao:
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")

    compra = Compra(
        usuario_id=sessao.usuario_id,
        voo_id=dados.voo_id
    )
    
    db.add(compra)
    db.commit()
    db.refresh(compra)
    
    return CompraResponse(
        id=compra.id,
        usuario_id=compra.usuario_id,
        voo_id=compra.voo_id,
        localizador=compra.localizador, 
        tickets=compra.tickets,
        data_compra=compra.data_compra
    )