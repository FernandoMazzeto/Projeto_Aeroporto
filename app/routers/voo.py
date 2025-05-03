from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.voo import Voo
from app.schemas.voo import VooResponse
from datetime import datetime

router = APIRouter(prefix="/voos", tags=["Voos"])

@router.get("/", response_model=list[VooResponse])
def listar_voos(
    origem_id: int = Query(...),
    destino_id: int = Query(...),
    data_partida: datetime = Query(...),
    db: Session = Depends(get_db)
):
    voos = db.query(Voo).filter(
        Voo.origem_id == origem_id,
        Voo.destino_id == destino_id,
        Voo.data_partida >= data_partida
    ).all()
    return voos