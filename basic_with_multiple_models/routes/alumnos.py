from fastapi import APIRouter, status

from dependencies.dependencies import DBAlumnosDep
from models.alumno import AlumnoUpsert, Error
from models.public import AlumnoBase, AlumnoFull

router = APIRouter()


@router.get("/")
def list(db: DBAlumnosDep) -> list[AlumnoBase]:
    return db.list()


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DBAlumnosDep, padron: int) -> AlumnoFull:
    return db.find(padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(db: DBAlumnosDep, alumno_a_crear: AlumnoUpsert) -> AlumnoBase:
    alumno = db.add(alumno_a_crear)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(db: DBAlumnosDep, padron: int, alumno_actualizado: AlumnoUpsert) -> AlumnoFull:
    alumno = db.update(padron, alumno_actualizado)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(db: DBAlumnosDep, padron: int) -> AlumnoFull:
    alumno = db.delete(padron)
    return alumno


@router.put("/{padron}/cargar_nota", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def cargar_nota(db: DBAlumnosDep, padron: int, nota: int) -> AlumnoFull:
    alumno = db.cargar_nota(padron, nota)
    return alumno
