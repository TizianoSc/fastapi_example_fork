from itertools import count

from pydantic import BaseModel, Field

from models.alumno import Alumno

_id_counter = count(1)


class Grupo(BaseModel):
    id: int = Field(default_factory=lambda: next(_id_counter))
    nombre: str
    nota: int = Field(gt=0, le=10)
    integrantes: list[Alumno] | None = []
