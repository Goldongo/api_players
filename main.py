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

@app.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

@app.get("/players/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players

@app.get("/players/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.get("/players/name/{name}", response_model=list[schemas.Player])
def read_player_by_name(name: str, db: Session = Depends(get_db)):
    players = crud.get_player_by_name(db, name=name)
    if not players:
        raise HTTPException(status_code=404, detail="Player not found")
    return players

@app.get("/players/position/{position}", response_model=list[schemas.Player])
def read_player_by_position(position: str, db: Session = Depends(get_db)):
    players = crud.get_player_by_position(db, position=position)
    if not players:
        raise HTTPException(status_code=404, detail="Player not found")
    return players

@app.post("/players/load_csv/")
def load_players_from_csv(db: Session = Depends(get_db)):
    crud.create_players_from_csv(db, "Dataset_Players.csv")
    return {"detail": "Players loaded from CSV"}
