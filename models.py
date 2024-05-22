from sqlalchemy import Column, Integer, String
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    position = Column(String(255), index=True)
    overall = Column(Integer)
