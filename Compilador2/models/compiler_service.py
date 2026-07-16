"""
models/compiler_service.py
-----------------------------
Corazon del "Modelo" en la arquitectura MVC: coordina las tres fases del
compilador sobre un archivo fuente y devuelve un ResultadoAnalisis listo
para que el controlador lo convierta en JSON.

Fases, en orden estricto (si una falla, no se continua a la siguiente):
    1) Lexica     -> PyLiteLexer     + EscuchaErroresLexicos
    2) Sintactica -> PyLiteParser    + EscuchaErroresSintacticos
    3) Semantica  -> VisitorSemantico (patron Visitor de ANTLR)

Nota: PyLiteLexer y PyLiteParser (generados por ANTLR) se importan aqui
de forma directa porque app.py agrega la carpeta generated/ al
sys.path antes de cargar este modulo. Sus nombres NO se traducen porque
son las clases reales generadas por la herramienta ANTLR.
"""

from antlr4 import InputStream, CommonTokenStream

from PyLiteLexer import PyLiteLexer
from PyLiteParser import PyLiteParser
from PyLiteParserVisitor import PyLiteParserVisitor

from models.analysis_result import ResultadoAnalisis, ErrorCompilador, FASE_LEXICA
from models.error_listener import EscuchaErroresLexicos, EscuchaErroresSintacticos
from models.semantic_visitor import crear_clase_visitor_semantico

# La clase del visitor semantico hereda de PyLiteParserVisitor (generada
# por ANTLR), asi que se construye una sola vez aqui, ya con ambas
# clases generadas disponibles.
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

    resultado.conteo_tokens = len([t for t in flujo_tokens.tokens if t.type != PyLiteParser.EOF])

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
    resultado.funciones_encontradas = visitor.tabla_simbolos.todos_los_nombres_funciones()
    resultado.variables_encontradas = visitor.tabla_simbolos.todos_los_nombres_variables()
    vista_previa = arbol.toStringTree(recog=analizador_sintactico)
    if len(vista_previa) > max_caracteres_vista_arbol:
        vista_previa = vista_previa[:max_caracteres_vista_arbol] + " ...(truncado)"
    resultado.vista_previa_arbol = vista_previa
    return resultado


def _contar_nodos_regla(arbol):
    """Cuenta cuantos nodos de regla (no terminales) tiene el arbol de
    analisis sintactico; se muestra como dato informativo junto al
    numero de tokens en la interfaz."""
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
