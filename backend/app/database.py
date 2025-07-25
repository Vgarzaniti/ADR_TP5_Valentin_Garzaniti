from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambiá los valores según tu configuración de MySQL
USER = "root"
PASSWORD = "Mimosito04"
HOST = "db"  # o IP de tu servidor
PORT = "3306"
DB_NAME = "libros_db"

# Usando pymysql como driver
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Mimosito04@db:3306/libros_db"

# Si usás mysqlclient como driver (más rápido, pero requiere compilación)
# SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Importante para MySQL
    pool_recycle=3600    # Evita timeout de conexión
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
