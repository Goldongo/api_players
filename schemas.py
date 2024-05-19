from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    position: str
    overall: int

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True
