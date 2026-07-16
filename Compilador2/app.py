"""
app.py
-------
Punto de entrada de la aplicacion. Crea la instancia de Flask, carga la
configuracion y registra el controlador (Blueprint). Se mantiene
deliberadamente minimo: la logica de negocio vive en models/ y las
rutas en controllers/, siguiendo la arquitectura MVC solicitada.
"""

import os
import sys

DIR_BASE = os.path.dirname(os.path.abspath(__file__))
DIR_GENERADOS = os.path.join(DIR_BASE, "generated")
if DIR_GENERADOS not in sys.path:
    sys.path.insert(0, DIR_GENERADOS)

from flask import Flask

from config import Config
from controllers.analysis_controller import plano_analisis


def crear_aplicacion():
    aplicacion = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="static",
    )
    aplicacion.config.from_object(Config)

    os.makedirs(aplicacion.config["CARPETA_SUBIDAS"], exist_ok=True)

    aplicacion.register_blueprint(plano_analisis)
    return aplicacion


# NOTA: la variable de modulo se deja llamada "app" (no "aplicacion")
# porque herramientas externas de despliegue de Flask (por ejemplo
# `flask run` o gunicorn "app:app") buscan por convencion una variable
# con ese nombre exacto dentro de app.py; renombrarla podria dejar de
# funcionar con esas herramientas aunque "python app.py" siga sirviendo.
app = crear_aplicacion()

if __name__ == "__main__":
    # host=0.0.0.0 para poder probarlo tambien desde otra maquina de
    # la red local si hace falta; debug=True solo para desarrollo.
    app.run(host="0.0.0.0", port=5000, debug=True)
