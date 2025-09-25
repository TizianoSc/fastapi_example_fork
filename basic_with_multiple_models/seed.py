import csv
import os
import random

from dependencies.dependencies import get_database_alumnos, get_database_grupos
from models.alumno import Alumno
from models.grupo import Grupo

src_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))


def seed():
    cargar_alumnos(os.path.join(src_root, "resources", "alumnos.csv"))
    cargar_grupos(os.path.join(src_root, "resources", "grupos.csv"))
    cargar_alumnos_grupos_relacion(os.path.join(src_root, "resources", "alumnos_grupos.csv"))


def cargar_alumnos(path):
    alumnos = []
    with open(path) as f:
        csvFile = csv.DictReader(f, delimiter=";")
        for linea in csvFile:
            alumnos.append(
                Alumno(
                    padron=int(linea["Padron"]),
                    nombre=linea["Nombre"],
                    apellido=linea["Apellido"],
                    edad=random.randint(18, 35),
                )
            )
    get_database_alumnos().cargar_alumnos(sorted(alumnos, key=lambda x: x.padron))


def cargar_grupos(path):
    grupos = []
    with open(path) as f:
        csvFile = csv.DictReader(f, delimiter=";")
        for linea in csvFile:
            grupos.append(
                Grupo(
                    nombre=linea["Nombre"],
                    nota=int(linea["Nota"]),
                )
            )
    get_database_grupos().cargar_grupos(sorted(grupos, key=lambda x: x.nombre))


def cargar_alumnos_grupos_relacion(path):
    with open(path) as f:
        csvFile = csv.DictReader(f, delimiter=";")
        for linea in csvFile:
            padron = int(linea["Padron"])
            grupo_id = int(linea["GrupoId"])
            alumno = get_database_alumnos().find(padron)
            get_database_grupos().agregar_integrante(grupo_id, alumno)
