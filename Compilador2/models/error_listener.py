"""
models/error_listener.py
--------------------------
ANTLR notifica los errores lexicos y sintacticos mediante la interfaz
ErrorListener. Aqui se definen dos listeners propios (uno para el lexer
y otro para el parser) que, en lugar de imprimir a stderr como hace el
listener por omision, acumulan cada error como un objeto ErrorCompilador
con la fase exacta, la linea, la columna y un mensaje en espaniol.
"""

from antlr4.error.ErrorListener import ErrorListener
from models.analysis_result import ErrorCompilador, FASE_LEXICA, FASE_SINTACTICA


class EscuchaErroresBase(ErrorListener):
    """Listener base que solo acumula errores en una lista.

    NOTA: el metodo syntaxError() no se puede renombrar; su nombre y su
    firma de parametros son parte de la interfaz ErrorListener de ANTLR,
    que invoca este metodo internamente con ese nombre exacto.
    """

    def __init__(self, fase):
        super().__init__()
        self.fase = fase
        self.errores = []

    def syntaxError(self, reconocedor, simbolo_conflictivo, linea, columna, msg, e):
        self.errores.append(
            ErrorCompilador(
                fase=self.fase,
                linea=linea,
                columna=columna + 1,  # ANTLR usa columnas base 0
                mensaje=self._traducir(msg, simbolo_conflictivo),
            )
        )

    def tiene_errores(self):
        return len(self.errores) > 0

    @staticmethod
    def _traducir(msg, simbolo_conflictivo):
        return msg


class EscuchaErroresLexicos(EscuchaErroresBase):
    """Captura caracteres que no corresponden a ningun token valido
    de la gramatica (por ejemplo, un simbolo como '@' o '$' fuera de
    cualquier regla lexica definida)."""

    def __init__(self):
        super().__init__(FASE_LEXICA)

    @staticmethod
    def _traducir(msg, simbolo_conflictivo):
        if "token recognition error" in msg:
            return msg.replace(
                "token recognition error at:",
                "caracter no reconocido por la gramatica:"
            )
        return msg


class EscuchaErroresSintacticos(EscuchaErroresBase):
    """Captura violaciones de la estructura gramatical: parentesis sin
    cerrar, falta de ':' en una sentencia compuesta, indentacion
    inconsistente, tokens inesperados, etc."""

    def __init__(self):
        super().__init__(FASE_SINTACTICA)

    @staticmethod
    def _traducir(msg, simbolo_conflictivo):
        traducciones = {
            "mismatched input": "entrada inesperada",
            "missing": "falta",
            "extraneous input": "entrada sobrante",
            "no viable alternative at input": "no existe una alternativa valida para la entrada",
        }
        salida = msg
        for en, es in traducciones.items():
            if salida.startswith(en):
                salida = salida.replace(en, es, 1)
                break
        return salida
