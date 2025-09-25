from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from database.database import Database
from dependencies.dependencies import get_database
from main import app
from models.models import Alumno

client = TestClient(app)

mock_db = MagicMock(Database)
app.dependency_overrides[get_database] = lambda: mock_db


juanp = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)
mariap = Alumno(padron=2, nombre="Maria", apellido="Lopez", edad=22)
juanp_data = {"nombre": "Juan", "apellido": "Perez", "edad": 20}


def test_get_alumnos():
    mock_db.list.return_value = [
        juanp,
        mariap,
    ]

    response = client.get(
        "/alumnos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2


def test_get_alumno():
    mock_db.find.return_value = juanp

    response = client.get(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_create_alumno():
    mock_db.add.return_value = juanp

    response = client.post("/alumnos/", json=juanp_data)

    assert response.status_code == 201
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_update_alumno():
    mock_db.update.return_value = juanp

    response = client.put("/alumnos/1", json=juanp_data)

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_delete_alumno():
    mock_db.delete.return_value = juanp

    response = client.delete(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20
