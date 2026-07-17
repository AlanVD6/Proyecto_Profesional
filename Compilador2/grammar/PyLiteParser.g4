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
    | PASAR
    | ROMPER
    | CONTINUAR
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
    : RETORNAR expr?
    ;

compoundStmt
    : ifStmt
    | whileStmt
    | forStmt
    | funcDef
    ;

ifStmt
    : SI expr DOS_PUNTOS block (SINO_SI expr DOS_PUNTOS block)* (SINO DOS_PUNTOS block)?
    ;

whileStmt
    : MIENTRAS expr DOS_PUNTOS block
    ;

forStmt
    : PARA ID EN expr DOS_PUNTOS block
    ;

funcDef
    : DEFINIR ID PARENTESIS_IZQUIERDO paramList? PARENTESIS_DERECHO DOS_PUNTOS block
    ;

paramList
    : ID (COMA ID)*
    ;

block
    : NUEVA_LINEA INDENTACION statement+ DESINDENTACION
    | simpleStmt
    ;

expr
    : expr PARENTESIS_IZQUIERDO argList? PARENTESIS_DERECHO             # callExpr
    | expr CORCHETE_IZQUIERDO expr CORCHETE_DERECHO                     # indexExpr
    | <assoc=right> expr POR POR expr                                  # powerExpr
    | (SUMA | RESTA) expr                                               # unaryExpr
    | expr (POR | DIVISION | DIVISION_ENTERA | MODULO) expr             # mulExpr
    | expr (SUMA | RESTA) expr                                          # addExpr
    | expr (IGUAL_QUE | DISTINTO_DE | MENOR_QUE | MAYOR_QUE | MENOR_O_IGUAL_QUE | MAYOR_O_IGUAL_QUE) expr # compareExpr
    | NO expr                                                           # notExpr
    | expr Y expr                                                       # andExpr
    | expr O expr                                                       # orExpr
    | atom                                                              # atomExpr
    ;

argList
    : expr (COMA expr)*
    ;

atom
    : ID                                    # nameAtom
    | ENTERO                                # intAtom
    | FLOTANTE                              # floatAtom
    | CADENA                                # stringAtom
    | VERDADERO                             # trueAtom
    | FALSO                                 # falseAtom
    | NULO                                  # noneAtom
    | PARENTESIS_IZQUIERDO expr PARENTESIS_DERECHO # parenAtom
    ;
