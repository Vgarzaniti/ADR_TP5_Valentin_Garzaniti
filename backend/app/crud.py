from sqlalchemy.orm import Session
from app import models, schemas

# ---- OPERACIONES CRUD PARA LIBROS ----
def create_libro(db: Session, libro: schemas.LibroCreate):
    db_libro = models.Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        anio=libro.anio
    )
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    
    # Asociar géneros
    for genero_id in libro.generos:
        genero = db.query(models.Genero).filter(models.Genero.id == genero_id).first()
        if genero:
            db_libro.generos.append(genero)
    db.commit()
    return db_libro

def get_libros(db: Session, skip: int = 0, limit: int = 100, search: str = None, ordering: str = None):
    query = db.query(models.Libro)
    
    if search:
        query = query.filter(
            models.Libro.titulo.ilike(f"%{search}%") | 
            models.Libro.autor.ilike(f"%{search}%")
        )
    
    if ordering == "asc":
        query = query.order_by(models.Libro.anio.asc())
    elif ordering == "desc":
        query = query.order_by(models.Libro.anio.desc())
    
    return query.offset(skip).limit(limit).all()

def get_libro(db: Session, libro_id: int):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()

def update_libro(db: Session, libro_id: int, libro: schemas.LibroUpdate):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not db_libro:
        return None
    
    # Actualizar campos básicos
    db_libro.titulo = libro.titulo
    db_libro.autor = libro.autor
    db_libro.anio = libro.anio
    
    # Actualizar géneros
    db_libro.generos = []
    for genero_id in libro.generos:
        genero = db.query(models.Genero).filter(models.Genero.id == genero_id).first()
        if genero:
            db_libro.generos.append(genero)
    
    db.commit()
    db.refresh(db_libro)
    return db_libro

def delete_libro(db: Session, libro_id: int):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if db_libro:
        db.delete(db_libro)
        db.commit()
        return True
    return False

# ---- OPERACIONES SOLO GET PARA GÉNEROS ----
def get_generos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Genero).offset(skip).limit(limit).all()

def get_genero(db: Session, genero_id: int):
    return db.query(models.Genero).filter(models.Genero.id == genero_id).first()