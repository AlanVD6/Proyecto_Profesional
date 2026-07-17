from antlr4 import InputStream, CommonTokenStream

from PyLiteLexer import PyLiteLexer
from PyLiteParser import PyLiteParser
from PyLiteParserVisitor import PyLiteParserVisitor

from models.analysis_result import ResultadoAnalisis, ErrorCompilador, FASE_LEXICA
from models.error_listener import EscuchaErroresLexicos, EscuchaErroresSintacticos
from models.semantic_visitor import crear_clase_visitor_semantico
from models.nombres_es import nombre_token_es, nombre_regla_es

VisitorSemantico = crear_clase_visitor_semantico(PyLiteParserVisitor, PyLiteParser)


def analizar_codigo_fuente(codigo_fuente, nombre_archivo, max_caracteres_vista_arbol=4000, **_ignorado):
    """Ejecuta las tres fases sobre `codigo_fuente` (str) y regresa un
    ResultadoAnalisis completo. Los errores propios del codigo analizado
    se reportan dentro del resultado, nunca como excepcion."""

    resultado = ResultadoAnalisis(nombre_archivo=nombre_archivo)

    # -------------------- FASE 1: ANALISIS LEXICO --------------------
    try:
        analizador_lexico = PyLiteLexer(InputStream(codigo_fuente))
        analizador_lexico.removeErrorListeners()
        escucha_lexica = EscuchaErroresLexicos()
        analizador_lexico.addErrorListener(escucha_lexica)

        flujo_tokens = CommonTokenStream(analizador_lexico)
        flujo_tokens.fill()
    except Exception as exc:
        resultado.agregar_error(ErrorCompilador(
            fase=FASE_LEXICA, linea=0, columna=0,
            mensaje=f"error interno del analizador lexico: {exc}"
        ))
        return resultado

    tokens_utiles = [t for t in flujo_tokens.tokens if t.type != PyLiteParser.EOF]
    resultado.conteo_tokens = len(tokens_utiles)
    resultado.tabla_tokens = _construir_tabla_tokens(tokens_utiles, analizador_lexico.symbolicNames)

    if escucha_lexica.tiene_errores():
        for e in escucha_lexica.errores:
            resultado.agregar_error(e)
        return resultado

    # ------------------ FASE 2: ANALISIS SINTACTICO -------------------
    flujo_tokens.reset()
    analizador_sintactico = PyLiteParser(flujo_tokens)
    analizador_sintactico.removeErrorListeners()
    escucha_sintactica = EscuchaErroresSintacticos()
    analizador_sintactico.addErrorListener(escucha_sintactica)

    arbol = analizador_sintactico.program()

    if escucha_sintactica.tiene_errores():
        for e in escucha_sintactica.errores:
            resultado.agregar_error(e)
        return resultado

    resultado.conteo_reglas = _contar_nodos_regla(arbol)

    # ------------------- FASE 3: ANALISIS SEMANTICO --------------------
    visitor = VisitorSemantico()
    errores_semanticos = visitor.analizar(arbol)

    if errores_semanticos:
        for e in errores_semanticos:
            resultado.agregar_error(e)
        return resultado

    # ------------------------- EXITO TOTAL ------------------------------
    resultado.exito = True
    vista_previa = _arbol_a_texto_es(arbol)
    if len(vista_previa) > max_caracteres_vista_arbol:
        vista_previa = vista_previa[:max_caracteres_vista_arbol] + " ...(truncado)"
    resultado.vista_previa_arbol = vista_previa
    return resultado


def _construir_tabla_tokens(tokens, nombres_simbolicos):
    tabla = []
    for t in tokens:
        nombre_simbolico = nombres_simbolicos[t.type] if 0 <= t.type < len(nombres_simbolicos) else str(t.type)
        tabla.append({
            "token": nombre_token_es(nombre_simbolico),
            "lexema": t.text,
        })
    return tabla


def _arbol_a_texto_es(nodo):
    from antlr4.tree.Tree import TerminalNode
    from antlr4.Utils import escapeWhitespace

    if isinstance(nodo, TerminalNode):
        return escapeWhitespace(nodo.getText(), False)

    hijos = [_arbol_a_texto_es(nodo.getChild(i)) for i in range(nodo.getChildCount())]
    etiqueta = nombre_regla_es(nodo)
    if hijos:
        return "(" + etiqueta + " " + " ".join(hijos) + ")"
    return "(" + etiqueta + ")"


def _contar_nodos_regla(arbol):
    from antlr4.tree.Tree import RuleNode
    conteo = 0
    pila = [arbol]
    while pila:
        nodo = pila.pop()
        if isinstance(nodo, RuleNode):
            conteo += 1
        for i in range(nodo.getChildCount()):
            pila.append(nodo.getChild(i))
    return conteo
