from pydantic import BaseModel

class JugadorBase(BaseModel):
    nombre: str
    posicion: str
    overall: int

class JugadorCreate(JugadorBase):
    pass

class Jugador(JugadorBase):
    id: int

    class Config:
        orm_mode = True
