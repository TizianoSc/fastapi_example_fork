import pytest
from fastapi import HTTPException

from database.grupo import DBGrupos
from models.alumno import Alumno
from models.grupo import Grupo

juan = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)
manuelin = Alumno(padron=2, nombre="Manuelin", apellido="Equis", edad=21)

grupo1 = Grupo(nombre="Grupo 1", nota=8)
grupo2 = Grupo(nombre="Grupo 2", nota=9)


@pytest.fixture
def db():
    return DBGrupos()


class TestDBGrupos:
    def test_cargar_grupos_vacio(self, db):
        assert db.grupos == []

    def test_cargar_grupos(self, db):
        db.cargar_grupos([grupo1, grupo2])
        assert db.grupos == [grupo1, grupo2]

    def test_find_valido(self, db):
        db.cargar_grupos([grupo1, grupo2])
        assert db.find(grupo2.id) == grupo2

    def test_find_no_existente(self, db):
        db.cargar_grupos([grupo1])
        with pytest.raises(HTTPException, match="404: Grupo not found"):
            db.find(999)

    def test_agregar_integrante(self, db):
        db.cargar_grupos([grupo1])
        db.agregar_integrante(grupo1.id, juan)
        assert juan in db.find(grupo1.id).integrantes
