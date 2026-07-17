parser grammar PyLiteParser;
options {
    tokenVocab = PyLiteLexer;
}

program
    : NUEVA_LINEA* statement* EOF
    ;

statement
    : simpleStmt
    | compoundStmt
    ;

simpleStmt
    : smallStmt (PUNTO_Y_COMA smallStmt)* PUNTO_Y_COMA? NUEVA_LINEA
    ;

smallStmt
    : assignStmt
    | exprStmt
    | returnStmt
    | PASS
    | BREAK
    | CONTINUE
    ;

assignStmt
    : ID assignOp expr
    ;

assignOp
    : IGUAL | IGUAL_SUMA | IGUAL_RESTA | IGUAL_POR | IGUAL_DIVISION
    ;

exprStmt
    : expr
    ;

returnStmt
    : RETURN expr?
    ;

compoundStmt
    : ifStmt
    | whileStmt
    | forStmt
    | funcDef
    ;

ifStmt
    : IF expr DOS_PUNTOS block (ELIF expr DOS_PUNTOS block)* (ELSE DOS_PUNTOS block)?
    ;

whileStmt
    : WHILE expr DOS_PUNTOS block
    ;

forStmt
    : FOR ID IN expr DOS_PUNTOS block
    ;

funcDef
    : DEF ID PARENTESIS_IZQUIERDO paramList? PARENTESIS_DERECHO DOS_PUNTOS block
    ;

paramList
    : ID (COMA ID)*
    ;

block
    : NUEVA_LINEA INDENTACION statement+ DESINDENTACION
    | simpleStmt
    ;

expr
    : expr PARENTESIS_IZQUIERDO argList? PARENTESIS_DERECHO                          # callExpr
    | expr CORCHETE_IZQUIERDO expr CORCHETE_DERECHO                          # indexExpr
    | <assoc=right> expr POR POR expr                    # powerExpr
    | (SUMA | RESTA) expr                                  # unaryExpr
    | expr (POR | DIVISION | DIVISION_ENTERA | MODULO) expr     # mulExpr
    | expr (SUMA | RESTA) expr                             # addExpr
    | expr (IGUAL_QUE | DISTINTO_DE | MENOR_QUE | MAYOR_QUE | MENOR_O_IGUAL_QUE | MAYOR_O_IGUAL_QUE) expr              # compareExpr
    | NOT expr                                              # notExpr
    | expr AND expr                                         # andExpr
    | expr OR expr                                          # orExpr
    | atom                                                  # atomExpr
    ;

argList
    : expr (COMA expr)*
    ;

atom
    : ID                     # nameAtom
    | ENTERO                      # intAtom
    | FLOTANTE                    # floatAtom
    | CADENA                   # stringAtom
    | TRUE                     # trueAtom
    | FALSE                    # falseAtom
    | NONE                     # noneAtom
    | PARENTESIS_IZQUIERDO expr PARENTESIS_DERECHO       # parenAtom
    ;
