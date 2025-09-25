from pydantic import BaseModel


class AlumnoBase(BaseModel):
    padron: int
    nombre: str
    apellido: str
    edad: int


class GrupoBase(BaseModel):
    id: int
    nombre: str
    nota: int


class AlumnoFull(AlumnoBase):
    grupos: list[GrupoBase] | None = []


class GrupoFull(GrupoBase):
    integrantes: list[AlumnoBase] | None = []
