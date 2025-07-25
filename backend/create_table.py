from app.database import engine, Base
import app.models  # importa las clases de los modelos para que SQLAlchemy las registre

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")