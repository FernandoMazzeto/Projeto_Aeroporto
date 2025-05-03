from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.aeroporto import Aeroporto
from app.schemas.aeroporto import AeroportoResponse

router = APIRouter(prefix="/aeroportos", tags=["Aeroportos"])

@router.get("/", response_model=list[AeroportoResponse])
def listar_aeroportos(db: Session = Depends(get_db)):
    return db.query(Aeroporto).all()