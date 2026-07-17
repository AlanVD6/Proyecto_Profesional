
from antlr4.error.ErrorListener import ErrorListener
from models.analysis_result import ErrorCompilador, FASE_LEXICA, FASE_SINTACTICA

class EscuchaErroresBase(ErrorListener):
    def __init__(self, fase):
        super().__init__()
        self.fase = fase
        self.errores = []

    def syntaxError(self, reconocedor, simbolo_conflictivo, linea, columna, msg, e):
        self.errores.append(
            ErrorCompilador(
                fase=self.fase,
                linea=linea,
                columna=columna + 1,
                mensaje=self._traducir(msg, simbolo_conflictivo),
            )
        )

    def tiene_errores(self):
        return len(self.errores) > 0

    @staticmethod
    def _traducir(msg, simbolo_conflictivo):
        return msg


class EscuchaErroresLexicos(EscuchaErroresBase):
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
