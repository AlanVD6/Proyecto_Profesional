"""
controllers/analysis_controller.py
------------------------------------
Controlador (en el sentido MVC) que expone las rutas HTTP de la
aplicacion:

    GET  /              -> pagina principal (vista con el formulario)
    POST /api/analyze   -> recibe el archivo subido via AJAX, ejecuta
                            las tres fases del compilador a traves del
                            modelo (models.compiler_service) y responde
                            en JSON.

Este archivo NO contiene logica de analisis lexico/sintactico/semantico
en si misma: unicamente adapta la peticion HTTP de entrada y la
respuesta de salida, delegando el trabajo real al modelo.
"""

import os
from flask import Blueprint, render_template, request, jsonify, current_app

from models.compiler_service import analizar_codigo_fuente

plano_analisis = Blueprint("analisis", __name__)


def _extension_permitida(nombre_archivo):
    if "." not in nombre_archivo:
        return False
    extension = nombre_archivo.rsplit(".", 1)[1].lower()
    return extension in current_app.config["EXTENSIONES_PERMITIDAS"]


@plano_analisis.route("/")
def index():
    return render_template("index.html")


@plano_analisis.route("/api/analyze", methods=["POST"])
def analizar():
    if "archivo_fuente" not in request.files:
        return jsonify({"exito": False, "error_servidor": "No se recibio ningun archivo."}), 400

    archivo = request.files["archivo_fuente"]

    if archivo.filename == "":
        return jsonify({"exito": False, "error_servidor": "No se selecciono ningun archivo."}), 400

    if not _extension_permitida(archivo.filename):
        return jsonify({
            "exito": False,
            "error_servidor": "Extension no permitida. Sube un archivo .py o .txt."
        }), 400

    bytes_crudos = archivo.read()
    try:
        codigo_fuente = bytes_crudos.decode("utf-8")
    except UnicodeDecodeError:
        return jsonify({
            "exito": False,
            "error_servidor": "El archivo no esta codificado en UTF-8 valido."
        }), 400

    # Se guarda una copia en uploads/ (opcional, util para depuracion /
    # historial); no es necesaria para el analisis en si.
    try:
        ruta_subida = os.path.join(current_app.config["CARPETA_SUBIDAS"], archivo.filename)
        with open(ruta_subida, "w", encoding="utf-8") as f:
            f.write(codigo_fuente)
    except OSError:
        pass  # si no se puede escribir, no interrumpe el analisis

    resultado = analizar_codigo_fuente(
        codigo_fuente=codigo_fuente,
        nombre_archivo=archivo.filename,
        max_caracteres_vista_arbol=current_app.config["MAX_CARACTERES_VISTA_ARBOL"],
    )

    return jsonify(resultado.a_diccionario())
