from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.compra import Compra
from app.models.sessao import Sessao
from app.schemas.compra import CompraCreate, CompraResponse
from datetime import datetime

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.post("/", response_model=CompraResponse)
def comprar_passagem(dados: CompraCreate, db: Session = Depends(get_db)):
    sessao = db.query(Sessao).filter(Sessao.chave == dados.chave, Sessao.ativa == "S").first()
    if not sessao:
        raise HTTPException(status_code=401, detail="Sessão inválida")

    compra = Compra(
        usuario_id=sessao.usuario_id,
        voo_id=dados.voo_id,
        data_compra=datetime.now()
    )
    db.add(compra)
    db.commit()
    db.refresh(compra)
    return compra