"""
config.py
----------
Configuracion centralizada de la aplicacion Flask.

NOTA: SECRET_KEY y MAX_CONTENT_LENGTH se dejan con su nombre original
en ingles a proposito: son nombres de configuracion RESERVADOS que
Flask/Werkzeug leen internamente por ese nombre exacto (por ejemplo,
Flask usa MAX_CONTENT_LENGTH para rechazar automaticamente peticiones
demasiado grandes). Renombrarlos haria que Flask dejara de aplicar
esas reglas silenciosamente.
"""

import os

DIR_BASE = os.path.dirname(os.path.abspath(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave-de-desarrollo-pylite-compiler")
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB, mas que suficiente para un .py

    CARPETA_SUBIDAS = os.path.join(DIR_BASE, "uploads")
    CARPETA_GENERADOS = os.path.join(DIR_BASE, "generated")
    EXTENSIONES_PERMITIDAS = {"py", "txt"}
    MAX_CARACTERES_VISTA_ARBOL = 4000
