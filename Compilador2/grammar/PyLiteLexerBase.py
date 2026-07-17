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

        if token.type == self.NUEVA_LINEA:
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
        if self.abiertos > 0:
            return

        siguiente_caracter = self._input.LA(1)
        if siguiente_caracter in (ord('\n'), ord('\r'), ord('#'), Token.EOF):
            return

        self._ultimo_token = token
        self._tokens_pendientes.append(token)

        cima = self._indentaciones[-1]
        if ancho_indentacion > cima:
            self._indentaciones.append(ancho_indentacion)
            self._tokens_pendientes.append(
                self._crear_token(self.INDENTACION, "<INDENT>", token))
        else:
            while ancho_indentacion < self._indentaciones[-1]:
                self._indentaciones.pop()
                self._tokens_pendientes.append(
                    self._crear_token(self.DESINDENTACION, "<DEDENT>", token))

    def _manejar_fin_archivo(self, token):
        if not self._fin_alcanzado:
            self._fin_alcanzado = True
            if self._ultimo_token is not None and self._ultimo_token.type != self.NUEVA_LINEA:
                self._tokens_pendientes.append(
                    self._crear_token(self.NUEVA_LINEA, "\n", token))
            while len(self._indentaciones) > 1:
                self._indentaciones.pop()
                self._tokens_pendientes.append(
                    self._crear_token(self.DESINDENTACION, "<DEDENT>", token))
            self._tokens_pendientes.append(token)
            return self._tokens_pendientes.pop(0)
        return token

    @staticmethod
    def _ancho(espacios):
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
