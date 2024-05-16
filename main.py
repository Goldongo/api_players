from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/jugadores/", response_model=schemas.Jugador)
def create_jugador(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    db_jugador = models.Jugador(nombre=jugador.nombre, posicion=jugador.posicion, overall=jugador.overall)
    return crud.create_jugador(db=db, jugador=db_jugador)

@app.get("/jugadores/", response_model=list[schemas.Jugador])
def read_jugadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jugadores = crud.get_jugadores(db, skip=skip, limit=limit)
    return jugadores

@app.get("/jugadores/{jugador_id}", response_model=schemas.Jugador)
def read_jugador(jugador_id: int, db: Session = Depends(get_db)):
    db_jugador = crud.get_jugador(db, jugador_id=jugador_id)
    if db_jugador is None:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return db_jugador

@app.put("/jugadores/{jugador_id}", response_model=schemas.Jugador)
def update_jugador(jugador_id: int, jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.update_jugador(db, jugador_id=jugador_id, jugador=jugador)

@app.delete("/jugadores/{jugador_id}", response_model=schemas.Jugador)
def delete_jugador(jugador_id: int, db: Session = Depends(get_db)):
    return crud.delete_jugador(db, jugador_id=jugador_id)
