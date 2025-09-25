from typing import Annotated

from fastapi import Depends

from database.alumno import DBAlumnos
from database.grupo import DBGrupos

__database_instance_alumnos = None
__database_instance_grupos = None


def init_dep():
    global __database_instance_alumnos
    global __database_instance_grupos
    __database_instance_alumnos = DBAlumnos()
    __database_instance_grupos = DBGrupos()


def get_database_alumnos() -> DBAlumnos:
    global __database_instance_alumnos
    if __database_instance_alumnos is None:
        raise RuntimeError("DB instance not initialized.")
    return __database_instance_alumnos


def get_database_grupos() -> DBGrupos:
    global __database_instance_grupos
    if __database_instance_grupos is None:
        raise RuntimeError("DB instance not initialized.")
    return __database_instance_grupos


DBAlumnosDep = Annotated[DBAlumnos, Depends(get_database_alumnos)]
DBGruposDep = Annotated[DBGrupos, Depends(get_database_grupos)]
