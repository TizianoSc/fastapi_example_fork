from fastapi import HTTPException, status
from sqlmodel import Session, select

from models.alumno import Alumno, AlumnoUpsert

default_limit = 10


class Database:
    def cargar_alumnos(self, session: Session, alumnos: list[Alumno]):
        session.add_all(alumnos)
        session.commit()

    def list(self, session: Session, limit: int, offset: int) -> list[Alumno]:
        if not limit:
            limit = default_limit
        if not offset:
            offset = 0
        query = select(Alumno).limit(limit).offset(offset)
        alumnos = session.exec(query).all()
        return alumnos

    def add(self, session: Session, alumno_a_crear: AlumnoUpsert) -> Alumno:
        alumno = Alumno(**alumno_a_crear.model_dump())
        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def find(self, session: Session, padron: int) -> Alumno:
        alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

        if alumno:
            return alumno
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")

    def delete(self, session: Session, padron: int) -> Alumno:
        alumno = self.find(session, padron)
        session.delete(alumno)
        session.commit()
        return alumno

    def update(self, session: Session, padron: int, nuevo_alumno: AlumnoUpsert) -> Alumno:
        alumno = self.find(session, padron)
        update_dict = nuevo_alumno.model_dump(exclude_unset=True)
        alumno.sqlmodel_update(update_dict)

        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno
