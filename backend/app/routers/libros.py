from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Libro)
def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db=db, libro=libro)

@router.get("/", response_model=List[schemas.Libro])
def read_libros(
    skip: int = 0,
    limit: int = 100,
    search: str = None,
    ordering: str = None,
    db: Session = Depends(get_db)
):
    return crud.get_libros(db, skip=skip, limit=limit, search=search, ordering=ordering)

@router.get("/{libro_id}", response_model=schemas.Libro)
def read_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id=libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.put("/{libro_id}", response_model=schemas.Libro)
def update_libro(
    libro_id: int,
    libro: schemas.LibroUpdate,
    db: Session = Depends(get_db)
):
    db_libro = crud.update_libro(db=db, libro_id=libro_id, libro=libro)
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_libro

@router.delete("/{libro_id}")
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    if not crud.delete_libro(db=db, libro_id=libro_id):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"ok": True}