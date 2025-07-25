from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base


# Tabla de asociación para relación muchos-a-muchos (Libro-Género)
libro_genero = Table(
    "libro_genero",
    Base.metadata,
    Column("libro_id", Integer, ForeignKey("libros.id")),
    Column("genero_id", Integer, ForeignKey("generos.id")),
)

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    autor = Column(String(100))
    anio = Column(Integer)
    generos = relationship("Genero", secondary=libro_genero, back_populates="libros")

class Genero(Base):
    __tablename__ = "generos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    libros = relationship("Libro", secondary=libro_genero, back_populates="generos")