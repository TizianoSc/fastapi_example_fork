from fastapi import APIRouter, status

from dependencies.dependencies import DBGruposDep
from models.alumno import Error
from models.public import GrupoBase, GrupoFull

router = APIRouter()


@router.get("/")
def list(db: DBGruposDep) -> list[GrupoBase]:
    return db.list()


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DBGruposDep, id: int) -> GrupoFull:
    return db.find(id)
