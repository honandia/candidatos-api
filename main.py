from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configurar la base de datos SQLite con SQLAlchemy
DATABASE_URL = "sqlite:///./candidatos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modelo SQLAlchemy para la tabla de candidatos
class Candidato(Base):
    __tablename__ = "candidatos"
    
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)

# Definir los datos que esperamos recibir en el endpoint
class CandidatoCreate(BaseModel):
    dni: str
    nombre: str
    apellido: str

# Inicializar FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint POST para crear un nuevo candidato
@app.post("/candidato")
def crear_candidato(candidato: CandidatoCreate, db: Session = Depends(get_db)):
    # Verificar si ya existe un candidato con el mismo DNI
    db_candidato = db.query(Candidato).filter(Candidato.dni == candidato.dni).first()
    if db_candidato:
        raise HTTPException(status_code=400, detail="El candidato con este DNI ya existe")
    
    # Crear nuevo candidato
    nuevo_candidato = Candidato(dni=candidato.dni, nombre=candidato.nombre, apellido=candidato.apellido)
    
    # Guardar en la base de datos
    db.add(nuevo_candidato)
    db.commit()
    db.refresh(nuevo_candidato)
    
    return {"mensaje": "Candidato creado exitosamente", "candidato": nuevo_candidato}

