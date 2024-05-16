from sqlalchemy import Column, Integer, String
from .database import Base

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    posicion = Column(String, index=True)
    overall = Column(Integer)
