from app.database import SessionLocal
from app.models import Genero

def cargar_generos():
    generos = [
    "Ficción",
    "No Ficción",
    "Misterio",
    "Ciencia Ficción",
    "Romance",
    "Fantásía",
    "Aventura",
    "Histórico",
    "Biografía",
    "Autobiografía",
    "Poesía",
    "Drama",
    "Terror",
    "Thriller",
    "Distopía",
    "Humor",
    "Clásicos",
    "Juvenil",
    "Infantil",
    "Cómic",
    "Novela gráfica",
    "Educativo",
    "Autoayuda",
    "Psicología",
    "Filosofía",
    "Policial",
    "Crítica literaria",
    "Mitología",
    "Religioso",
    "Espiritualidad",
    "Viajes",
    "Cocina",
    "Arte",
    "Música",
    "Tecnología",
    "Ciencia",
    "Divulgación científica",
    "Negocios",
    "Economía",
    "Política",
    "Sociología",
    "Ecología",
    "Ensayo",
    "Teatro",
    "Deportes",
    "Erótico",
    "Satírico",
    "Realismo Mágico",
    "Western",
    "Steampunk",
    "Paranormal"
]
    db = SessionLocal()
    try:
        for nombre in generos:
            existe = db.query(Genero).filter(Genero.nombre == nombre).first()
            if not existe:
                db.add(Genero(nombre=nombre))
        db.commit()
        print("Seed de géneros completado")
    finally:
        db.close()

if __name__ == "__main__":
    cargar_generos()