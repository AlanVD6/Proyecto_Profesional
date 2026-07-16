"""
models/analysis_result.py
--------------------------
Estructuras de datos (modelo, en el sentido MVC) que representan el
resultado del analisis de un archivo fuente: en que fase se detuvo el
proceso, y el detalle de cada error encontrado.
"""

from dataclasses import dataclass, field


FASE_LEXICA = "lexico"
FASE_SINTACTICA = "sintactico"
FASE_SEMANTICA = "semantico"

ETIQUETAS_FASE = {
    FASE_LEXICA: "Analisis lexico",
    FASE_SINTACTICA: "Analisis sintactico",
    FASE_SEMANTICA: "Analisis semantico",
}


@dataclass
class ErrorCompilador:
    fase: str          # "lexico" | "sintactico" | "semantico"
    linea: int
    columna: int
    mensaje: str

    def a_diccionario(self):
        return {
            "fase": self.fase,
            "fase_etiqueta": ETIQUETAS_FASE.get(self.fase, self.fase),
            "linea": self.linea,
            "columna": self.columna,
            "mensaje": self.mensaje,
        }


@dataclass
class ResultadoAnalisis:
    exito: bool = True
    fase_detenida: str | None = None
    errores: list = field(default_factory=list)
    conteo_tokens: int = 0
    conteo_reglas: int = 0
    funciones_encontradas: list = field(default_factory=list)
    variables_encontradas: list = field(default_factory=list)
    vista_previa_arbol: str = ""
    nombre_archivo: str = ""

    def agregar_error(self, error: ErrorCompilador):
        self.errores.append(error)
        self.exito = False
        if self.fase_detenida is None:
            self.fase_detenida = error.fase

    def a_diccionario(self):
        return {
            "exito": self.exito,
            "fase_detenida": self.fase_detenida,
            "fase_detenida_etiqueta": ETIQUETAS_FASE.get(self.fase_detenida, None),
            "errores": [e.a_diccionario() for e in self.errores],
            "conteo_tokens": self.conteo_tokens,
            "conteo_reglas": self.conteo_reglas,
            "funciones_encontradas": self.funciones_encontradas,
            "variables_encontradas": self.variables_encontradas,
            "vista_previa_arbol": self.vista_previa_arbol,
            "nombre_archivo": self.nombre_archivo,
        }
