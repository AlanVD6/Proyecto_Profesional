
from models.symbol_table import TablaSimbolos
from models.analysis_result import ErrorCompilador, FASE_SEMANTICA


def crear_clase_visitor_semantico(ClaseVisitorGenerado, ClaseParserGenerado):
    class VisitorSemantico(ClaseVisitorGenerado):

        def __init__(self):
            self.tabla_simbolos = TablaSimbolos()
            self.errores = []
            self.profundidad_bucle = 0
            self.profundidad_funcion = 0

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

        def _recolectar_firmas_funciones(self, ctx):
            if isinstance(ctx, ClaseParserGenerado.FuncDefContext):
                nombre = ctx.ID().getText()
                num_parametros = len(ctx.paramList().ID()) if ctx.paramList() else 0
                if self.tabla_simbolos.definir_funcion(nombre, num_parametros):
                    self._error(ctx.ID().getSymbol(),
                        f"la funcion '{nombre}' ya habia sido definida antes (SEM05)")
            for i in range(ctx.getChildCount()):
                hijo = ctx.getChild(i)
                if hasattr(hijo, "getChildCount"):
                    self._recolectar_firmas_funciones(hijo)
        def visitAssignStmt(self, ctx):
            nombre = ctx.ID().getText()
            operador = ctx.assignOp().getText()

            if operador != "=" and not self.tabla_simbolos.esta_definida(nombre):
                self._error(ctx.ID().getSymbol(),
                    f"la variable '{nombre}' se usa con '{operador}' pero no ha sido "
                    f"declarada previamente (SEM02)")

            self.visit(ctx.expr())
            self.tabla_simbolos.definir_variable(nombre)
            return None

        def visitReturnStmt(self, ctx):
            if self.profundidad_funcion == 0:
                self._error(ctx.RETORNAR().getSymbol(),
                    "la sentencia 'return' se usa fuera de una funcion (SEM06)")
            if ctx.expr():
                self.visit(ctx.expr())
            return None

        def visitSmallStmt(self, ctx):
            if ctx.ROMPER() is not None and self.profundidad_bucle == 0:
                self._error(ctx.ROMPER().getSymbol(),
                    "la sentencia 'break' se usa fuera de un bucle (SEM07)")
            if ctx.CONTINUAR() is not None and self.profundidad_bucle == 0:
                self._error(ctx.CONTINUAR().getSymbol(),
                    "la sentencia 'continue' se usa fuera de un bucle (SEM07)")
            return self.visitChildren(ctx)

        def visitWhileStmt(self, ctx):
            self.visit(ctx.expr())
            self.profundidad_bucle += 1
            self.visit(ctx.block())
            self.profundidad_bucle -= 1
            return None

        def visitForStmt(self, ctx):
            self.visit(ctx.expr())
            self.tabla_simbolos.definir_variable(ctx.ID().getText())
            self.profundidad_bucle += 1
            self.visit(ctx.block())
            self.profundidad_bucle -= 1
            return None

        def visitFuncDef(self, ctx):
            self.tabla_simbolos.apilar_ambito(ctx.ID().getText())
            if ctx.paramList():
                for token_nombre in ctx.paramList().ID():
                    self.tabla_simbolos.definir_variable(token_nombre.getText())
            self.profundidad_funcion += 1
            self.visit(ctx.block())
            self.profundidad_funcion -= 1
            self.tabla_simbolos.desapilar_ambito()
            return None

        def visitAtomExpr(self, ctx):
            atomo = ctx.atom()
            if isinstance(atomo, ClaseParserGenerado.NameAtomContext):
                self._verificar_uso_variable(atomo.ID().getText(), atomo.ID().getSymbol())
                return None
            return self.visitChildren(ctx)

        def visitCallExpr(self, ctx):
            invocado = ctx.expr()
            if isinstance(invocado, ClaseParserGenerado.AtomExprContext) and \
               isinstance(invocado.atom(), ClaseParserGenerado.NameAtomContext):
                token_nombre = invocado.atom().ID()
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
