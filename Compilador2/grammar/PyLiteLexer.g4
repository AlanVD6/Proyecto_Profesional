lexer grammar PyLiteLexer;

// =======================================================================
// Gramatica lexica de PyLite.
//
// Incluye el catalogo COMPLETO de palabras reservadas, operadores y
// signos de puntuacion documentados en la investigacion de Python
// (35 palabras clave + operadores aritmeticos, relacionales, logicos,
// de asignacion compuesta, de identidad/pertenencia + delimitadores).
//
// El PARSER (PyLiteParser.g4) solo usa un subconjunto practico de estos
// tokens para construir sentencias (if/while/for/def, expresiones,
// etc). El resto de palabras reservadas (class, try, import, lambda...)
// se reconocen correctamente a nivel LEXICO -tal como pide el informe-
// aunque todavia no tengan una regla SINTACTICA que las use; si
// aparecen en un programa, el analizador se detendra en la fase
// sintactica indicando que esa construccion aun no esta soportada.
// =======================================================================

tokens { INDENT, DEDENT }

options {
    superClass = PyLiteLexerBase;
}

// -----------------------------------------------------------------------
// Palabras reservadas (35, segun la documentacion oficial de Python)
// -----------------------------------------------------------------------
FALSE    : 'False';
AWAIT    : 'await';
ELSE     : 'else';
IMPORT   : 'import';
PASS     : 'pass';
NONE     : 'None';
BREAK    : 'break';
EXCEPT   : 'except';
IN       : 'in';
RAISE    : 'raise';
TRUE     : 'True';
CLASS    : 'class';
FINALLY  : 'finally';
IS       : 'is';
RETURN   : 'return';
AND      : 'and';
CONTINUE : 'continue';
FOR      : 'for';
LAMBDA   : 'lambda';
TRY      : 'try';
AS       : 'as';
DEF      : 'def';
FROM     : 'from';
NONLOCAL : 'nonlocal';
WHILE    : 'while';
ASSERT   : 'assert';
DEL      : 'del';
GLOBAL   : 'global';
NOT      : 'not';
WITH     : 'with';
ASYNC    : 'async';
ELIF     : 'elif';
IF       : 'if';
OR       : 'or';
YIELD    : 'yield';

// -----------------------------------------------------------------------
// Operadores aritmeticos
// -----------------------------------------------------------------------
PLUS        : '+';
MINUS       : '-';
STAR        : '*';
DOUBLESTAR  : '**';
SLASH       : '/';
DOUBLESLASH : '//';
PERCENT     : '%';

// -----------------------------------------------------------------------
// Operadores relacionales (de comparacion)
// -----------------------------------------------------------------------
EQ  : '==';
NEQ : '!=';
LE  : '<=';
GE  : '>=';
LT  : '<';
GT  : '>';

// -----------------------------------------------------------------------
// Operadores de asignacion (simple y compuestos)
// -----------------------------------------------------------------------
ASSIGN         : '=';
PLUS_ASSIGN    : '+=';
MINUS_ASSIGN   : '-=';
STAR_ASSIGN    : '*=';
SLASH_ASSIGN   : '/=';
DSLASH_ASSIGN  : '//=';
PERCENT_ASSIGN : '%=';
POWER_ASSIGN   : '**=';
AMP_ASSIGN     : '&=';
PIPE_ASSIGN    : '|=';
CARET_ASSIGN   : '^=';
RSHIFT_ASSIGN  : '>>=';
LSHIFT_ASSIGN  : '<<=';
WALRUS         : ':=';

// -----------------------------------------------------------------------
// Operadores a nivel de bits
// -----------------------------------------------------------------------
AMP     : '&';
PIPE    : '|';
CARET   : '^';
TILDE   : '~';
LSHIFT  : '<<';
RSHIFT  : '>>';

// -----------------------------------------------------------------------
// Delimitadores y puntuacion
// -----------------------------------------------------------------------
LPAREN   : '(' { self.abiertos += 1 };
RPAREN   : ')' { self.abiertos -= 1 };
LBRACKET : '[' { self.abiertos += 1 };
RBRACKET : ']' { self.abiertos -= 1 };
LBRACE   : '{' { self.abiertos += 1 };
RBRACE   : '}' { self.abiertos -= 1 };

COMMA    : ',';
COLON    : ':';
DOT      : '.';
SEMI     : ';';
AT       : '@';
ARROW    : '->';
ELLIPSIS : '...';

// -----------------------------------------------------------------------
// Identificadores y literales
// -----------------------------------------------------------------------
NAME : [a-zA-Z_][a-zA-Z_0-9]*;

// Enteros: decimal, hexadecimal, octal y binario, con guion bajo
// como separador de legibilidad (8_100_000_000, 0xFF, 0o755, 0b1011).
INT
    : [0-9] ('_'? [0-9])*
    | '0' [xX] HEX_DIGIT ('_'? HEX_DIGIT)*
    | '0' [oO] [0-7] ('_'? [0-7])*
    | '0' [bB] [01] ('_'? [01])*
    ;
fragment HEX_DIGIT : [0-9a-fA-F];

// Flotantes: con punto decimal y/o notacion cientifica (3e8, 6.626e-34).
FLOAT
    : DIGITS '.' DIGITS? EXPONENT?
    | '.' DIGITS EXPONENT?
    | DIGITS EXPONENT
    ;
fragment DIGITS   : [0-9] ('_'? [0-9])*;
fragment EXPONENT : [eE] [+-]? DIGITS;

STRING
    : '"' (~["\\\r\n] | '\\' .)* '"'
    | '\'' (~['\\\r\n] | '\\' .)* '\''
    ;

// -----------------------------------------------------------------------
// Comentarios y espacios en blanco
// -----------------------------------------------------------------------
COMMENT : '#' ~[\r\n]* -> skip;

// Espacios/tabs que NO estan al inicio de linea (los del inicio de linea
// los consume la propia regla NEWLINE para poder medir la indentacion).
WS : [ \t]+ -> skip;

// El salto de linea real, junto con la sangria de la linea siguiente.
// El procesamiento de INDENT/DEDENT ocurre en PyLiteLexerBase.nextToken().
NEWLINE : ('\r'? '\n' | '\r') [ \t]*;
