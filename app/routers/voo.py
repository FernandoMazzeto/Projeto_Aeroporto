from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List

from app.database import get_db
from app.models.voo import Voo
from app.schemas.voo import VooResponse

router = APIRouter(prefix="/voos", tags=["Voos"])

@router.get("/", response_model=List[VooResponse], summary="Listar voos por origem, destino e data")
def listar_voos(
    origem_id: int = Query(..., description="ID do aeroporto de origem"),
    destino_id: int = Query(..., description="ID do aeroporto de destino"),
    data_partida: datetime = Query(..., description="Data no formato YYYY-MM-DD"),
    db: Session = Depends(get_db)
):
    
    try:
        voos = db.query(Voo).filter(
            Voo.origem_id == origem_id,
            Voo.destino_id == destino_id,
            Voo.data_partida >= data_partida,
            Voo.data_partida < data_partida + timedelta(days=1)  
        ).all()
        
        if not voos:
            raise HTTPException(
                status_code=404,
                detail="Nenhum voo encontrado para os filtros aplicados"
            )
            
        return voos

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar voos: {str(e)}"
        )

@router.get("/menor-tarifa", response_model=List[VooResponse], summary="Buscar voos com menor tarifa")
def pesquisar_voos(
    origem_id: int = Query(..., description="ID do aeroporto de origem"),
    destino_id: int = Query(..., description="ID do aeroporto de destino"),
    passageiros: int = Query(1, gt=0, description="Número de passageiros"),
    db: Session = Depends(get_db)
):
    """
    **Demanda Item 7**: Retorna os voos com as menores tarifas para o número de passageiros.
    """
    try:
        voos = db.query(Voo).filter(
            Voo.origem_id == origem_id,
            Voo.destino_id == destino_id,
            Voo.data_partida >= datetime.now()  
        ).order_by(
            Voo.preco
        ).limit(
            passageiros
        ).all()
        
        if not voos:
            raise HTTPException(
                status_code=404,
                detail="Nenhum voo disponível para esta rota"
            )
            
        return voos

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro na pesquisa: {str(e)}"
        )