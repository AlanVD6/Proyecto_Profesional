lexer grammar PyLiteLexer;
tokens { INDENTACION, DESINDENTACION }

options {
    superClass = PyLiteLexerBase;
}
// Palabras reservadas 
FALSE : 'False';
AWAIT : 'await';
ELSE : 'else';
IMPORT : 'import';
PASS : 'pass';
NONE : 'None';
BREAK : 'break';
EXCEPT : 'except';
IN : 'in';
RAISE : 'raise';
TRUE : 'True';
CLASS : 'class';
FINALLY : 'finally';
IS : 'is';
RETURN : 'return';
AND : 'and';
CONTINUE : 'continue';
FOR : 'for';
LAMBDA     : 'lambda';
TRY : 'try';
AS : 'as';
DEF : 'def';
FROM : 'from';
NONLOCAL : 'nonlocal';
WHILE : 'while';
ASSERT: 'assert';
DEL : 'del';
GLOBAL : 'global';
NOT : 'not';
WITH : 'with';
ASYNC : 'async';
ELIF : 'elif';
IF : 'if';
OR : 'or';
YIELD : 'yield';

// Operadores aritmeticos

SUMA            : '+';
RESTA           : '-';
POR             : '*';
POTENCIA        : '**';
DIVISION        : '/';
DIVISION_ENTERA : '//';
MODULO          : '%';

// Operadores relacionales (de comparacion)
IGUAL_QUE         : '==';
DISTINTO_DE       : '!=';
MENOR_O_IGUAL_QUE : '<=';
MAYOR_O_IGUAL_QUE : '>=';
MENOR_QUE         : '<';
MAYOR_QUE         : '>';

// Operadores de asignacion (simple y compuestos)
IGUAL                  : '=';
IGUAL_SUMA             : '+=';
IGUAL_RESTA            : '-=';
IGUAL_POR              : '*=';
IGUAL_DIVISION         : '/=';
IGUAL_DIVISION_ENTERA  : '//=';
IGUAL_MODULO           : '%=';
IGUAL_POTENCIA         : '**=';
IGUAL_AND_BIT          : '&=';
IGUAL_OR_BIT           : '|=';
IGUAL_XOR_BIT          : '^=';
IGUAL_DESPLAZ_DER      : '>>=';
IGUAL_DESPLAZ_IZQ      : '<<=';
IGUAL_EN_EXPRESION     : ':=';

// Operadores a nivel de bits
AND_BIT                  : '&';
OR_BIT                   : '|';
XOR_BIT                  : '^';
NEGACION_BIT              : '~';
DESPLAZAMIENTO_IZQUIERDA  : '<<';
DESPLAZAMIENTO_DERECHA    : '>>';

// Delimitadores y puntuacion
PARENTESIS_IZQUIERDO : '(' { self.abiertos += 1 };
PARENTESIS_DERECHO   : ')' { self.abiertos -= 1 };
CORCHETE_IZQUIERDO   : '[' { self.abiertos += 1 };
CORCHETE_DERECHO     : ']' { self.abiertos -= 1 };
LLAVE_IZQUIERDA      : '{' { self.abiertos += 1 };
LLAVE_DERECHA        : '}' { self.abiertos -= 1 };

COMA               : ',';
DOS_PUNTOS         : ':';
PUNTO              : '.';
PUNTO_Y_COMA       : ';';
ARROBA             : '@';
FLECHA             : '->';
PUNTOS_SUSPENSIVOS : '...';

// Identificadores y literales
ID : [a-zA-Z_][a-zA-Z_0-9]*;
ENTERO
    : [0-9] ('_'? [0-9])*
    | '0' [xX] HEX_DIGIT ('_'? HEX_DIGIT)*
    | '0' [oO] [0-7] ('_'? [0-7])*
    | '0' [bB] [01] ('_'? [01])*
    ;
fragment HEX_DIGIT : [0-9a-fA-F];
FLOTANTE
    : DIGITS '.' DIGITS? EXPONENT?
    | '.' DIGITS EXPONENT?
    | DIGITS EXPONENT
    ;
fragment DIGITS   : [0-9] ('_'? [0-9])*;
fragment EXPONENT : [eE] [+-]? DIGITS;

CADENA
    : '"' (~["\\\r\n] | '\\' .)* '"'
    | '\'' (~['\\\r\n] | '\\' .)* '\''
    ;

COMENTARIO : '#' ~[\r\n]* -> skip;
ESPACIOS : [ \t]+ -> skip;
NUEVA_LINEA : ('\r'? '\n' | '\r') [ \t]*;
