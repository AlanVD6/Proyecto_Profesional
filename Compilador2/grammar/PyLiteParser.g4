parser grammar PyLiteParser;
options {
    tokenVocab = PyLiteLexer;
}

program
    : NEWLINE* statement* EOF
    ;

statement
    : simpleStmt
    | compoundStmt
    ;

simpleStmt
    : smallStmt (SEMI smallStmt)* SEMI? NEWLINE
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
    : NAME assignOp expr
    ;

assignOp
    : ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN
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
    : IF expr COLON block (ELIF expr COLON block)* (ELSE COLON block)?
    ;

whileStmt
    : WHILE expr COLON block
    ;

forStmt
    : FOR NAME IN expr COLON block
    ;

funcDef
    : DEF NAME LPAREN paramList? RPAREN COLON block
    ;

paramList
    : NAME (COMMA NAME)*
    ;

block
    : NEWLINE INDENT statement+ DEDENT
    | simpleStmt
    ;

expr
    : expr LPAREN argList? RPAREN                          # callExpr
    | expr LBRACKET expr RBRACKET                          # indexExpr
    | <assoc=right> expr STAR STAR expr                    # powerExpr
    | (PLUS | MINUS) expr                                  # unaryExpr
    | expr (STAR | SLASH | DOUBLESLASH | PERCENT) expr     # mulExpr
    | expr (PLUS | MINUS) expr                             # addExpr
    | expr (EQ | NEQ | LT | GT | LE | GE) expr              # compareExpr
    | NOT expr                                              # notExpr
    | expr AND expr                                         # andExpr
    | expr OR expr                                          # orExpr
    | atom                                                  # atomExpr
    ;

argList
    : expr (COMMA expr)*
    ;

atom
    : NAME                     # nameAtom
    | INT                      # intAtom
    | FLOAT                    # floatAtom
    | STRING                   # stringAtom
    | TRUE                     # trueAtom
    | FALSE                    # falseAtom
    | NONE                     # noneAtom
    | LPAREN expr RPAREN       # parenAtom
    ;
