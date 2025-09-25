from fastapi import HTTPException, status

from models.alumno import Alumno, AlumnoUpsert


class DBAlumnos:
    def __init__(self):
        self.alumnos = []

    def cargar_alumnos(self, alumnos: list[Alumno]):
        self.alumnos = alumnos

    def list(self) -> list[Alumno]:
        return self.alumnos

    def add(self, alumno_a_crear: AlumnoUpsert) -> Alumno:
        padron = len(self.alumnos) + 1
        alumno = Alumno(
            nombre=alumno_a_crear.nombre,
            apellido=alumno_a_crear.apellido,
            edad=alumno_a_crear.edad,
            padron=padron,
        )
        self.alumnos.append(alumno)
        return alumno

    def find(self, padron: int) -> Alumno:
        for alumno in self.alumnos:
            if alumno.padron == padron:
                return alumno
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")

    def delete(self, padron: int) -> Alumno:
        alumno = self.find(padron)
        self.alumnos.remove(alumno)
        return alumno

    def update(self, padron: int, nuevo_alumno: AlumnoUpsert) -> Alumno:
        alumno = self.find(padron)
        alumno.nombre = nuevo_alumno.nombre
        alumno.apellido = nuevo_alumno.apellido
        alumno.edad = nuevo_alumno.edad
        return alumno

    def cargar_nota(self, padron: int, nota: int) -> Alumno:
        alumno = self.find(padron)
        alumno.notas.append(nota)
        return alumno
