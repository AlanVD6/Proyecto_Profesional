import os

DIR_BASE = os.path.dirname(os.path.abspath(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave-de-desarrollo-pylite-compiler")
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

    CARPETA_SUBIDAS = os.path.join(DIR_BASE, "uploads")
    CARPETA_GENERADOS = os.path.join(DIR_BASE, "generated")
    EXTENSIONES_PERMITIDAS = {"py", "txt"}
    MAX_CARACTERES_VISTA_ARBOL = 4000
