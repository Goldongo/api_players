from sqlalchemy.orm import Session
from . import models, schemas

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player_by_name(db: Session, name: str):
    return db.query(models.Player).filter(models.Player.name == name).all()

def get_player_by_position(db: Session, position: str):
    return db.query(models.Player).filter(models.Player.position == position).all()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def create_players_from_csv(db: Session, csv_file: str):
    import csv
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = models.Player(name=row['name'], position=row['position'], overall=int(row['overall']))
            db.add(player)
        db.commit()