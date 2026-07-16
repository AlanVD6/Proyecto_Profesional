"""
PyLiteLexerBase.py
-------------------
Clase base para el lexer generado por ANTLR (PyLiteLexer).

Python es un lenguaje sensible a la indentacion: los bloques de codigo
(cuerpos de if/while/for/def) no se delimitan con llaves sino con el nivel
de sangria de cada linea. Una gramatica libre de contexto "pura" no puede
expresar esa regla, asi que se resuelve aqui, en el lexer, insertando
tokens sinteticos INDENT y DEDENT antes de que el texto llegue al parser.

Algoritmo (variante simplificada de la usada por la gramatica oficial
Python3 de antlr/grammars-v4):

1. Se mantiene una pila `_indentaciones` con los niveles de sangria abiertos
   (siempre inicia en [0], la columna base del archivo).
2. La regla lexica NEWLINE reconoce el salto de linea real MAS los
   espacios/tabs que le siguen (o sea, ya incluye la sangria de la
   siguiente linea en su propio texto).
3. Si la siguiente linea esta vacia, es un comentario, o es EOF, ese
   NEWLINE se descarta por completo (no representa el fin de una
   sentencia real) y se sigue leyendo.
4. En otro caso, se compara el ancho de esa sangria contra la cima de
   la pila:
   - mayor  -> se apila y se emite un token INDENT
   - menor  -> se desapilan niveles y se emite un DEDENT por cada uno
   - igual  -> no se emite nada adicional, solo el NEWLINE
5. Dentro de parentesis o corchetes abiertos ('(' '[') los saltos de
   linea se ignoran por completo, gracias al contador `abiertos`
   (Python permite partir una expresion en varias lineas ahi dentro).
6. Al llegar a EOF se cierran todos los niveles de indentacion
   pendientes, emitiendo los DEDENT que falten antes del token EOF.

IMPORTANTE: __init__, reset() y nextToken() NO se pueden renombrar: son
metodos de la clase Lexer de antlr4-python3-runtime que ANTLR invoca
internamente por ese nombre exacto. Lo mismo aplica a self.NEWLINE,
self.INDENT, self.DEDENT (constantes de tipo de token heredadas de la
subclase generada PyLiteLexer) y a self._input (atributo interno de la
clase base Lexer). El atributo `abiertos` SI se puede traducir, pero
debe coincidir exactamente con el nombre usado en las acciones
incrustadas de grammar/PyLiteLexer.g4 ({ self.abiertos += 1 }, etc.),
las cuales ya se actualizaron para mantener la consistencia.
"""

from antlr4 import Lexer
from antlr4.Token import Token, CommonToken


class PyLiteLexerBase(Lexer):

    def __init__(self, input=None, output=None):
        super().__init__(input, output)
        self._tokens_pendientes = []
        self._indentaciones = [0]
        self.abiertos = 0
        self._ultimo_token = None
        self._fin_alcanzado = False

    def reset(self):
        self._tokens_pendientes = []
        self._indentaciones = [0]
        self.abiertos = 0
        self._ultimo_token = None
        self._fin_alcanzado = False
        super().reset()

    def nextToken(self):
        if self._tokens_pendientes:
            return self._tokens_pendientes.pop(0)

        token = super().nextToken()

        if token.type == Token.EOF:
            return self._manejar_fin_archivo(token)

        if token.type == self.NEWLINE:
            self._procesar_salto_linea(token)
            if self._tokens_pendientes:
                return self._tokens_pendientes.pop(0)
            return self.nextToken()

        self._ultimo_token = token
        return token

    # ------------------------------------------------------------------
    def _procesar_salto_linea(self, token):
        texto = token.text
        ultimo_salto = max(texto.rfind('\n'), texto.rfind('\r'))
        texto_indentacion = texto[ultimo_salto + 1:] if ultimo_salto >= 0 else ''
        ancho_indentacion = self._ancho(texto_indentacion)

        # Dentro de parentesis/corchetes abiertos, Python ignora saltos
        # de linea por completo (continuacion implicita).
        if self.abiertos > 0:
            return

        siguiente_caracter = self._input.LA(1)
        if siguiente_caracter in (ord('\n'), ord('\r'), ord('#'), Token.EOF):
            # Linea en blanco, comentario o fin de archivo: no cuenta
            # como fin real de sentencia.
            return

        self._ultimo_token = token
        self._tokens_pendientes.append(token)

        cima = self._indentaciones[-1]
        if ancho_indentacion > cima:
            self._indentaciones.append(ancho_indentacion)
            self._tokens_pendientes.append(
                self._crear_token(self.INDENT, "<INDENT>", token))
        else:
            while ancho_indentacion < self._indentaciones[-1]:
                self._indentaciones.pop()
                self._tokens_pendientes.append(
                    self._crear_token(self.DEDENT, "<DEDENT>", token))

    def _manejar_fin_archivo(self, token):
        if not self._fin_alcanzado:
            self._fin_alcanzado = True
            if self._ultimo_token is not None and self._ultimo_token.type != self.NEWLINE:
                self._tokens_pendientes.append(
                    self._crear_token(self.NEWLINE, "\n", token))
            while len(self._indentaciones) > 1:
                self._indentaciones.pop()
                self._tokens_pendientes.append(
                    self._crear_token(self.DEDENT, "<DEDENT>", token))
            self._tokens_pendientes.append(token)
            return self._tokens_pendientes.pop(0)
        return token

    @staticmethod
    def _ancho(espacios):
        """Ancho efectivo de una cadena de indentacion; cada tab avanza
        al siguiente multiplo de 8 (comportamiento estandar de Python)."""
        ancho = 0
        for caracter in espacios:
            if caracter == '\t':
                ancho += 8 - (ancho % 8)
            else:
                ancho += 1
        return ancho

    def _crear_token(self, tipo_token, texto, token_referencia):
        t = CommonToken(
            source=(self, self._input),
            type=tipo_token,
            channel=Token.DEFAULT_CHANNEL,
            start=token_referencia.stop + 1,
            stop=token_referencia.stop
        )
        t.text = texto
        t.line = token_referencia.line
        t.column = token_referencia.column
        return t
