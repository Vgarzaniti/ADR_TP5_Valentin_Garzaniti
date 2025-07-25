from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Genero])
def read_generos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_generos(db, skip=skip, limit=limit)

@router.get("/{genero_id}", response_model=schemas.Genero)
def read_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = crud.get_genero(db, genero_id=genero_id)
    if not genero:
        raise HTTPException(status_code=404, detail="Género no encontrado")
    return genero