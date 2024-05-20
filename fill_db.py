import csv
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Player
import os

def create_players_from_csv(db: Session, csv_file: str):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = Player(name=row['name'], position=row['position'], overall=int(row['overall']))
            db.add(player)
        db.commit()

if __name__ == "__main__":
    # Verifica si la base de datos está vacía
    db = SessionLocal()
    if not db.query(Player).first():
        csv_file_path = "/mnt/data/Dataset_Players (1).csv"  # Asegúrate de que esta ruta sea correcta
        create_players_from_csv(db, csv_file_path)
    db.close()
