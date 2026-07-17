lexer grammar PyLiteLexer;
tokens { INDENT, DEDENT }

options {
    superClass = PyLiteLexerBase;
}
// Palabras reservadas 
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

// Operadores aritmeticos

PLUS        : '+';
MINUS       : '-';
STAR        : '*';
DOUBLESTAR  : '**';
SLASH       : '/';
DOUBLESLASH : '//';
PERCENT     : '%';

// Operadores relacionales (de comparacion)
EQ  : '==';
NEQ : '!=';
LE  : '<=';
GE  : '>=';
LT  : '<';
GT  : '>';

// Operadores de asignacion (simple y compuestos)
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

// Operadores a nivel de bits
AMP     : '&';
PIPE    : '|';
CARET   : '^';
TILDE   : '~';
LSHIFT  : '<<';
RSHIFT  : '>>';

// Delimitadores y puntuacion
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

// Identificadores y literales
NAME : [a-zA-Z_][a-zA-Z_0-9]*;
INT
    : [0-9] ('_'? [0-9])*
    | '0' [xX] HEX_DIGIT ('_'? HEX_DIGIT)*
    | '0' [oO] [0-7] ('_'? [0-7])*
    | '0' [bB] [01] ('_'? [01])*
    ;
fragment HEX_DIGIT : [0-9a-fA-F];
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

COMMENT : '#' ~[\r\n]* -> skip;
WS : [ \t]+ -> skip;
NEWLINE : ('\r'? '\n' | '\r') [ \t]*;
