from pydantic import BaseModel
from typing import List, Optional

# Esquemas para Géneros (solo GET)
class GeneroBase(BaseModel):
    nombre: str

class GeneroCreate(GeneroBase):
    pass

class Genero(GeneroBase):
    id: int
    class Config:
        from_attributes = True

# Esquemas para Libros (CRUD completo)
class LibroBase(BaseModel):
    titulo: str
    autor: str
    anio: int

class LibroCreate(LibroBase):
    generos: List[int] = []  # Lista de IDs de géneros

class LibroUpdate(LibroBase):
    generos: List[int] = []

class Libro(LibroBase):
    id: int
    generos: List[Genero] = []  # Lista de objetos Genero completos
    class Config:
        from_attributes = True