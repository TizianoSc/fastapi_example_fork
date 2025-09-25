from fastapi import APIRouter, status

from dependencies.database import DatabaseDep
from dependencies.sqlmodel import SessionDep
from models.alumno import Alumno, AlumnoUpsert, Error

router = APIRouter()


@router.get("/")
def list(session: SessionDep, db: DatabaseDep, limit: int | None = None, offset: int | None = None) -> list[Alumno]:
    return db.list(session, limit, offset)


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, db: DatabaseDep, padron: int) -> Alumno:
    return db.find(session, padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, db: DatabaseDep, alumno_a_crear: AlumnoUpsert) -> Alumno:
    alumno = db.add(session, alumno_a_crear)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(session: SessionDep, db: DatabaseDep, padron: int, alumno_actualizado: AlumnoUpsert) -> Alumno:
    alumno = db.update(session, padron, alumno_actualizado)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(session: SessionDep, db: DatabaseDep, padron: int) -> Alumno:
    alumno = db.delete(session, padron)
    return alumno
