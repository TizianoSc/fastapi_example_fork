from fastapi import HTTPException, status

from models.alumno import Alumno
from models.grupo import Grupo


class DBGrupos:
    def __init__(self):
        self.grupos = []

    def cargar_grupos(self, grupos: list[Grupo]):
        self.grupos = grupos

    def list(self) -> list[Grupo]:
        return self.grupos

    def find(self, id: int) -> Grupo:
        for grupo in self.grupos:
            if grupo.id == id:
                return grupo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found")

    def agregar_integrante(self, id: int, alumno: Alumno):
        grupo = self.find(id)
        grupo.integrantes.append(alumno)
