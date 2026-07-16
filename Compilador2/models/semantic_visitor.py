"""
models/semantic_visitor.py
----------------------------
Analizador semantico. Se hereda directamente de PyLiteParserVisitor (la
clase que ANTLR genera automaticamente) y se sobreescribe un metodo
visitX por cada regla que interesa revisar; en las demas, ANTLR sigue
bajando por el arbol solo (comportamiento por defecto: visitChildren),
igual que en los ejercicios de clase.

IMPORTANTE: los metodos visitAssignStmt, visitReturnStmt, visitSmallStmt,
visitWhileStmt, visitForStmt, visitFuncDef, visitAtomExpr, visitCallExpr
y visitMulExpr NO se pueden renombrar: ANTLR los invoca automaticamente
por ese nombre exacto (deriva del nombre de la regla/alternativa en la
gramatica). Lo mismo aplica a los accesos ctx.NAME(), ctx.expr(),
ctx.paramList(), etc., que son metodos generados por ANTLR.

Reglas semanticas revisadas:
  SEM01  Variable usada sin haber sido declarada antes.
  SEM02  Asignacion compuesta (+=, -=, ...) sobre variable inexistente.
  SEM03  Llamada a una funcion que no existe.
  SEM04  Numero de argumentos distinto al declarado en la funcion.
  SEM05  Redefinicion de una funcion ya declarada.
  SEM06  'return' fuera de una funcion.
  SEM07  'break' / 'continue' fuera de un bucle.
  SEM08  Division / modulo entre una constante 0.
"""

from models.symbol_table import TablaSimbolos
from models.analysis_result import ErrorCompilador, FASE_SEMANTICA


def crear_clase_visitor_semantico(ClaseVisitorGenerado, ClaseParserGenerado):
    """ClaseVisitorGenerado y ClaseParserGenerado se generan en tiempo de
    ejecucion (son producto de ANTLR), asi que la clase se construye
    aqui adentro para poder heredar de ellos directamente."""

    class VisitorSemantico(ClaseVisitorGenerado):

        def __init__(self):
            self.tabla_simbolos = TablaSimbolos()
            self.errores = []
            self.profundidad_bucle = 0
            self.profundidad_funcion = 0

        # ------------------------------------------------------------
        def analizar(self, arbol):
            self._recolectar_firmas_funciones(arbol)
            self.visit(arbol)
            return self.errores

        def _error(self, token, mensaje):
            self.errores.append(ErrorCompilador(
                fase=FASE_SEMANTICA,
                linea=token.line,
                columna=token.column + 1,
                mensaje=mensaje,
            ))

        # ------------------------------------------------------------
        # Pre-escaneo: registra todas las funciones del archivo antes
        # de revisar los cuerpos, para permitir llamadas hacia adelante.
        # ------------------------------------------------------------
        def _recolectar_firmas_funciones(self, ctx):
            if isinstance(ctx, ClaseParserGenerado.FuncDefContext):
                nombre = ctx.NAME().getText()
                num_parametros = len(ctx.paramList().NAME()) if ctx.paramList() else 0
                if self.tabla_simbolos.definir_funcion(nombre, num_parametros):
                    self._error(ctx.NAME().getSymbol(),
                        f"la funcion '{nombre}' ya habia sido definida antes (SEM05)")
            for i in range(ctx.getChildCount()):
                hijo = ctx.getChild(i)
                if hasattr(hijo, "getChildCount"):
                    self._recolectar_firmas_funciones(hijo)

        # ------------------------------------------------------------
        # Asignaciones: registran la variable en la tabla de simbolos
        # ------------------------------------------------------------
        def visitAssignStmt(self, ctx):
            nombre = ctx.NAME().getText()
            operador = ctx.assignOp().getText()

            if operador != "=" and not self.tabla_simbolos.esta_definida(nombre):
                self._error(ctx.NAME().getSymbol(),
                    f"la variable '{nombre}' se usa con '{operador}' pero no ha sido "
                    f"declarada previamente (SEM02)")

            self.visit(ctx.expr())
            self.tabla_simbolos.definir_variable(nombre)
            return None

        # ------------------------------------------------------------
        # return / break / continue
        # ------------------------------------------------------------
        def visitReturnStmt(self, ctx):
            if self.profundidad_funcion == 0:
                self._error(ctx.RETURN().getSymbol(),
                    "la sentencia 'return' se usa fuera de una funcion (SEM06)")
            if ctx.expr():
                self.visit(ctx.expr())
            return None

        def visitSmallStmt(self, ctx):
            if ctx.BREAK() is not None and self.profundidad_bucle == 0:
                self._error(ctx.BREAK().getSymbol(),
                    "la sentencia 'break' se usa fuera de un bucle (SEM07)")
            if ctx.CONTINUE() is not None and self.profundidad_bucle == 0:
                self._error(ctx.CONTINUE().getSymbol(),
                    "la sentencia 'continue' se usa fuera de un bucle (SEM07)")
            return self.visitChildren(ctx)

        # ------------------------------------------------------------
        # Bucles: llevan la cuenta de anidamiento para validar break/continue
        # ------------------------------------------------------------
        def visitWhileStmt(self, ctx):
            self.visit(ctx.expr())
            self.profundidad_bucle += 1
            self.visit(ctx.block())
            self.profundidad_bucle -= 1
            return None

        def visitForStmt(self, ctx):
            self.visit(ctx.expr())
            self.tabla_simbolos.definir_variable(ctx.NAME().getText())
            self.profundidad_bucle += 1
            self.visit(ctx.block())
            self.profundidad_bucle -= 1
            return None

        # ------------------------------------------------------------
        # Funciones: nuevo ambito con sus parametros ya definidos
        # ------------------------------------------------------------
        def visitFuncDef(self, ctx):
            self.tabla_simbolos.apilar_ambito(ctx.NAME().getText())
            if ctx.paramList():
                for token_nombre in ctx.paramList().NAME():
                    self.tabla_simbolos.definir_variable(token_nombre.getText())
            self.profundidad_funcion += 1
            self.visit(ctx.block())
            self.profundidad_funcion -= 1
            self.tabla_simbolos.desapilar_ambito()
            return None

        # ------------------------------------------------------------
        # Uso de un nombre "suelto" (no llamado): es una variable.
        # ------------------------------------------------------------
        def visitAtomExpr(self, ctx):
            atomo = ctx.atom()
            if isinstance(atomo, ClaseParserGenerado.NameAtomContext):
                self._verificar_uso_variable(atomo.NAME().getText(), atomo.NAME().getSymbol())
                return None
            return self.visitChildren(ctx)

        # ------------------------------------------------------------
        # Llamada a funcion: NOMBRE ( argumentos ).
        # ------------------------------------------------------------
        def visitCallExpr(self, ctx):
            invocado = ctx.expr()
            if isinstance(invocado, ClaseParserGenerado.AtomExprContext) and \
               isinstance(invocado.atom(), ClaseParserGenerado.NameAtomContext):
                token_nombre = invocado.atom().NAME()
                self._verificar_llamada_funcion(token_nombre.getText(), token_nombre.getSymbol(), ctx)
            else:
                self.visit(invocado)

            if ctx.argList():
                self.visit(ctx.argList())
            return None

        def _verificar_uso_variable(self, nombre, token):
            if not self.tabla_simbolos.esta_definida(nombre):
                self._error(token,
                    f"la variable '{nombre}' se usa pero no ha sido declarada "
                    f"antes en este ambito (SEM01)")

        def _verificar_llamada_funcion(self, nombre, token, ctx_llamada):
            if not self.tabla_simbolos.es_funcion(nombre):
                self._error(token,
                    f"se invoca a '{nombre}' como funcion, pero no existe "
                    f"ninguna funcion con ese nombre (SEM03)")
                return
            esperados = self.tabla_simbolos.num_parametros_funcion(nombre)
            lista_argumentos = ctx_llamada.argList()
            recibidos = len(lista_argumentos.expr()) if lista_argumentos else 0
            if esperados is not None and recibidos != esperados:
                self._error(token,
                    f"la funcion '{nombre}' espera {esperados} argumento(s), "
                    f"pero se le pasaron {recibidos} (SEM04)")

        # ------------------------------------------------------------
        # Division / modulo entre una constante 0
        # ------------------------------------------------------------
        def visitMulExpr(self, ctx):
            self.visitChildren(ctx)
            texto_operador = ctx.getChild(1).getText()
            if texto_operador in ("/", "//", "%"):
                derecho = ctx.expr(1)
                if self._es_cero_literal(derecho):
                    self._error(ctx.getChild(1).getSymbol(),
                        f"division entre cero detectada en tiempo de analisis "
                        f"('{texto_operador}' con divisor constante 0) (SEM08)")
            return None

        @staticmethod
        def _es_cero_literal(ctx_expr):
            try:
                return float(ctx_expr.getText()) == 0.0
            except ValueError:
                return False

    return VisitorSemantico
