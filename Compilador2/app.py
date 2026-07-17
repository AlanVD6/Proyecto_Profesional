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

app = crear_aplicacion()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
