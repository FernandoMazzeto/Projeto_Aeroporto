from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.voo import Voo
from app.models.aeroporto import Aeroporto
from app.schemas.aeroporto import AeroportoResponse

router = APIRouter(prefix="/aeroportos", tags=["Aeroportos"])

@router.get("/", response_model=list[AeroportoResponse])
def listar_aeroportos(db: Session = Depends(get_db)):
    return db.query(Aeroporto).all()

@router.get("/por-origem/{origem_id}", response_model=list[AeroportoResponse])
def aeroportos_por_origem(origem_id: int, db: Session = Depends(get_db)):
    destinos = db.query(Voo.destino_id).filter(Voo.origem_id == origem_id).distinct()
    return db.query(Aeroporto).filter(Aeroporto.id.in_(destinos)).all()