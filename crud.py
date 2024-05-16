from sqlalchemy.orm import Session

from . import models

def get_jugador(db: Session, jugador_id: int):
    return db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()

def get_jugadores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Jugador).offset(skip).limit(limit).all()

def create_jugador(db: Session, jugador: models.Jugador):
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    return jugador

def delete_jugador(db: Session, jugador_id: int):
    db_jugador = get_jugador(db, jugador_id)
    if db_jugador:
        db.delete(db_jugador)
        db.commit()
    return db_jugador

def update_jugador(db: Session, jugador_id: int, jugador: models.Jugador):
    db_jugador = get_jugador(db, jugador_id)
    if db_jugador:
        for key, value in jugador.dict().items():
            setattr(db_jugador, key, value)
        db.commit()
        db.refresh(db_jugador)
    return db_jugador

