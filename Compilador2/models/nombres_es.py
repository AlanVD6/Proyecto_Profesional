
NOMBRES_TOKENS_ES = {
    # Palabras reservadas
    "FALSE": "FALSO", "AWAIT": "ESPERAR", "ELSE": "SINO", "IMPORT": "IMPORTAR",
    "PASS": "PASAR", "NONE": "NULO", "BREAK": "ROMPER", "EXCEPT": "EXCEPTO",
    "IN": "EN", "RAISE": "LANZAR", "TRUE": "VERDADERO", "CLASS": "CLASE",
    "FINALLY": "FINALMENTE", "IS": "ES", "RETURN": "RETORNAR", "AND": "Y",
    "CONTINUE": "CONTINUAR", "FOR": "PARA", "LAMBDA": "LAMBDA", "TRY": "INTENTAR",
    "AS": "COMO", "DEF": "DEFINIR", "FROM": "DESDE", "NONLOCAL": "NO_LOCAL",
    "WHILE": "MIENTRAS", "ASSERT": "ASEGURAR", "DEL": "ELIMINAR", "GLOBAL": "GLOBAL",
    "NOT": "NO", "WITH": "CON", "ASYNC": "ASINCRONO", "ELIF": "SINO_SI",
    "IF": "SI", "OR": "O", "YIELD": "CEDER",

    # Operadores aritmeticos
    "PLUS": "SUMA", "MINUS": "RESTA", "STAR": "POR", "DOUBLESTAR": "POTENCIA",
    "SLASH": "DIVISION", "DOUBLESLASH": "DIVISION_ENTERA", "PERCENT": "MODULO",

    # Operadores relacionales
    "EQ": "IGUAL_QUE", "NEQ": "DISTINTO_DE", "LE": "MENOR_O_IGUAL_QUE",
    "GE": "MAYOR_O_IGUAL_QUE", "LT": "MENOR_QUE", "GT": "MAYOR_QUE",

    # Operadores de asignacion
    "ASSIGN": "ASIGNACION", "PLUS_ASSIGN": "ASIGNACION_SUMA",
    "MINUS_ASSIGN": "ASIGNACION_RESTA", "STAR_ASSIGN": "ASIGNACION_POR",
    "SLASH_ASSIGN": "ASIGNACION_DIVISION", "DSLASH_ASSIGN": "ASIGNACION_DIVISION_ENTERA",
    "PERCENT_ASSIGN": "ASIGNACION_MODULO", "POWER_ASSIGN": "ASIGNACION_POTENCIA",
    "AMP_ASSIGN": "ASIGNACION_AND_BIT", "PIPE_ASSIGN": "ASIGNACION_OR_BIT",
    "CARET_ASSIGN": "ASIGNACION_XOR_BIT", "RSHIFT_ASSIGN": "ASIGNACION_DESPLAZ_DER",
    "LSHIFT_ASSIGN": "ASIGNACION_DESPLAZ_IZQ", "WALRUS": "ASIGNACION_EN_EXPRESION",

    # Operadores a nivel de bits
    "AMP": "AND_BIT", "PIPE": "OR_BIT", "CARET": "XOR_BIT", "TILDE": "NEGACION_BIT",
    "LSHIFT": "DESPLAZAMIENTO_IZQUIERDA", "RSHIFT": "DESPLAZAMIENTO_DERECHA",

    # Delimitadores y puntuacion
    "LPAREN": "PARENTESIS_IZQUIERDO", "RPAREN": "PARENTESIS_DERECHO",
    "LBRACKET": "CORCHETE_IZQUIERDO", "RBRACKET": "CORCHETE_DERECHO",
    "LBRACE": "LLAVE_IZQUIERDA", "RBRACE": "LLAVE_DERECHA",
    "COMMA": "COMA", "COLON": "DOS_PUNTOS", "DOT": "PUNTO", "SEMI": "PUNTO_Y_COMA",
    "AT": "ARROBA", "ARROW": "FLECHA", "ELLIPSIS": "PUNTOS_SUSPENSIVOS",

    # Identificadores y literales
    "NAME": "ID",
    "INT": "ENTERO", "FLOAT": "FLOTANTE", "STRING": "CADENA",

    # Estructura de bloques / fin de linea
    "NEWLINE": "NUEVA_LINEA", "INDENT": "INDENTACION", "DEDENT": "DESINDENTACION",
}


def nombre_token_es(nombre_simbolico):
    """Devuelve el nombre en espaniol de un tipo de token; si no esta
    en el diccionario (caso que no deberia pasar), regresa el nombre
    original tal cual."""
    return NOMBRES_TOKENS_ES.get(nombre_simbolico, nombre_simbolico)

NOMBRES_REGLAS_ES = {
    "ProgramContext": "programa",
    "StatementContext": "sentencia",
    "SimpleStmtContext": "sentenciaSimple",
    "SmallStmtContext": "instruccion",
    "AssignStmtContext": "asignacion",
    "AssignOpContext": "operadorAsignacion",
    "ExprStmtContext": "expresionComoSentencia",
    "ReturnStmtContext": "sentenciaRetorno",
    "CompoundStmtContext": "sentenciaCompuesta",
    "IfStmtContext": "sentenciaSi",
    "WhileStmtContext": "sentenciaMientras",
    "ForStmtContext": "sentenciaPara",
    "FuncDefContext": "definicionFuncion",
    "ParamListContext": "listaParametros",
    "BlockContext": "bloque",
    "ArgListContext": "listaArgumentos",

    # Alternativas etiquetadas de "expr"
    "CallExprContext": "llamadaFuncion",
    "IndexExprContext": "indexacion",
    "PowerExprContext": "potencia",
    "UnaryExprContext": "signoUnario",
    "MulExprContext": "multiplicacionDivision",
    "AddExprContext": "sumaResta",
    "CompareExprContext": "comparacion",
    "NotExprContext": "negacionLogica",
    "AndExprContext": "conjuncionY",
    "OrExprContext": "disyuncionO",
    "AtomExprContext": "atomo",

    # Alternativas etiquetadas de "atom"
    "NameAtomContext": "identificador",
    "IntAtomContext": "literalEntero",
    "FloatAtomContext": "literalFlotante",
    "StringAtomContext": "literalCadena",
    "TrueAtomContext": "literalVerdadero",
    "FalseAtomContext": "literalFalso",
    "NoneAtomContext": "literalNulo",
    "ParenAtomContext": "expresionEntreParentesis",
}


def nombre_regla_es(nodo):
    """Devuelve el nombre en espaniol de un nodo del arbol sintactico a
    partir del nombre de su clase de contexto ANTLR (ej. AddExprContext
    -> 'sumaResta'). Si la clase no esta mapeada, regresa su nombre
    original sin el sufijo 'Context', como respaldo."""
    nombre_clase = type(nodo).__name__
    if nombre_clase in NOMBRES_REGLAS_ES:
        return NOMBRES_REGLAS_ES[nombre_clase]
    return nombre_clase[:-7] if nombre_clase.endswith("Context") else nombre_clase
