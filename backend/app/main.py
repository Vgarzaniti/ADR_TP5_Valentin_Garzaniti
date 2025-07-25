from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models 

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Configuración CORS EXTENDIDA (colocar ANTES de los routers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL exacta de tu frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Incluye tus routers después
from app.routers import libros, generos
app.include_router(libros.router, prefix="/api/libros")
app.include_router(generos.router, prefix="/api/generos")