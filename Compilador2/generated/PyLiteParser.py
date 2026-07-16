# Generated from PyLiteParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,90,219,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,3,1,53,8,
        1,1,2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,3,2,64,8,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,3,7,86,8,7,1,8,1,8,1,8,1,8,3,8,92,8,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,5,9,103,8,9,10,9,12,9,106,9,9,1,9,1,9,1,9,3,
        9,111,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,3,12,129,8,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,5,13,138,8,13,10,13,12,13,141,9,13,1,14,1,14,1,14,4,14,
        146,8,14,11,14,12,14,147,1,14,1,14,1,14,3,14,153,8,14,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,161,8,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,185,8,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,
        193,8,15,10,15,12,15,196,9,15,1,16,1,16,1,16,5,16,201,8,16,10,16,
        12,16,204,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,217,8,17,1,17,0,1,30,18,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,0,4,1,0,51,55,1,0,38,39,2,0,40,40,42,44,1,0,45,
        50,239,0,39,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,73,1,0,0,0,8,75,
        1,0,0,0,10,79,1,0,0,0,12,81,1,0,0,0,14,83,1,0,0,0,16,91,1,0,0,0,
        18,93,1,0,0,0,20,112,1,0,0,0,22,117,1,0,0,0,24,124,1,0,0,0,26,134,
        1,0,0,0,28,152,1,0,0,0,30,160,1,0,0,0,32,197,1,0,0,0,34,216,1,0,
        0,0,36,38,5,90,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,
        40,1,0,0,0,40,45,1,0,0,0,41,39,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,
        0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,
        1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,53,3,4,2,0,51,53,3,16,8,0,
        52,50,1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,59,3,6,3,0,55,56,5,80,
        0,0,56,58,3,6,3,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,
        1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,64,5,80,0,0,63,62,1,0,0,0,
        63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,90,0,0,66,5,1,0,0,0,67,74,3,
        8,4,0,68,74,3,12,6,0,69,74,3,14,7,0,70,74,5,7,0,0,71,74,5,9,0,0,
        72,74,5,19,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,
        0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,7,1,0,0,0,75,76,5,84,0,0,76,
        77,3,10,5,0,77,78,3,30,15,0,78,9,1,0,0,0,79,80,7,0,0,0,80,11,1,0,
        0,0,81,82,3,30,15,0,82,13,1,0,0,0,83,85,5,17,0,0,84,86,3,30,15,0,
        85,84,1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,0,87,92,3,18,9,0,88,92,3,
        20,10,0,89,92,3,22,11,0,90,92,3,24,12,0,91,87,1,0,0,0,91,88,1,0,
        0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,17,1,0,0,0,93,94,5,35,0,0,94,
        95,3,30,15,0,95,96,5,78,0,0,96,104,3,28,14,0,97,98,5,34,0,0,98,99,
        3,30,15,0,99,100,5,78,0,0,100,101,3,28,14,0,101,103,1,0,0,0,102,
        97,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,110,
        1,0,0,0,106,104,1,0,0,0,107,108,5,5,0,0,108,109,5,78,0,0,109,111,
        3,28,14,0,110,107,1,0,0,0,110,111,1,0,0,0,111,19,1,0,0,0,112,113,
        5,27,0,0,113,114,3,30,15,0,114,115,5,78,0,0,115,116,3,28,14,0,116,
        21,1,0,0,0,117,118,5,20,0,0,118,119,5,84,0,0,119,120,5,11,0,0,120,
        121,3,30,15,0,121,122,5,78,0,0,122,123,3,28,14,0,123,23,1,0,0,0,
        124,125,5,24,0,0,125,126,5,84,0,0,126,128,5,71,0,0,127,129,3,26,
        13,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,72,
        0,0,131,132,5,78,0,0,132,133,3,28,14,0,133,25,1,0,0,0,134,139,5,
        84,0,0,135,136,5,77,0,0,136,138,5,84,0,0,137,135,1,0,0,0,138,141,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,27,1,0,0,0,141,139,1,
        0,0,0,142,143,5,90,0,0,143,145,5,1,0,0,144,146,3,2,1,0,145,144,1,
        0,0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,149,1,
        0,0,0,149,150,5,2,0,0,150,153,1,0,0,0,151,153,3,4,2,0,152,142,1,
        0,0,0,152,151,1,0,0,0,153,29,1,0,0,0,154,155,6,15,-1,0,155,156,7,
        1,0,0,156,161,3,30,15,8,157,158,5,31,0,0,158,161,3,30,15,4,159,161,
        3,34,17,0,160,154,1,0,0,0,160,157,1,0,0,0,160,159,1,0,0,0,161,194,
        1,0,0,0,162,163,10,9,0,0,163,164,5,40,0,0,164,165,5,40,0,0,165,193,
        3,30,15,9,166,167,10,7,0,0,167,168,7,2,0,0,168,193,3,30,15,8,169,
        170,10,6,0,0,170,171,7,1,0,0,171,193,3,30,15,7,172,173,10,5,0,0,
        173,174,7,3,0,0,174,193,3,30,15,6,175,176,10,3,0,0,176,177,5,18,
        0,0,177,193,3,30,15,4,178,179,10,2,0,0,179,180,5,36,0,0,180,193,
        3,30,15,3,181,182,10,11,0,0,182,184,5,71,0,0,183,185,3,32,16,0,184,
        183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,193,5,72,0,0,187,
        188,10,10,0,0,188,189,5,73,0,0,189,190,3,30,15,0,190,191,5,74,0,
        0,191,193,1,0,0,0,192,162,1,0,0,0,192,166,1,0,0,0,192,169,1,0,0,
        0,192,172,1,0,0,0,192,175,1,0,0,0,192,178,1,0,0,0,192,181,1,0,0,
        0,192,187,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,
        0,195,31,1,0,0,0,196,194,1,0,0,0,197,202,3,30,15,0,198,199,5,77,
        0,0,199,201,3,30,15,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,
        0,0,0,202,203,1,0,0,0,203,33,1,0,0,0,204,202,1,0,0,0,205,217,5,84,
        0,0,206,217,5,85,0,0,207,217,5,86,0,0,208,217,5,87,0,0,209,217,5,
        13,0,0,210,217,5,3,0,0,211,217,5,8,0,0,212,213,5,71,0,0,213,214,
        3,30,15,0,214,215,5,72,0,0,215,217,1,0,0,0,216,205,1,0,0,0,216,206,
        1,0,0,0,216,207,1,0,0,0,216,208,1,0,0,0,216,209,1,0,0,0,216,210,
        1,0,0,0,216,211,1,0,0,0,216,212,1,0,0,0,217,35,1,0,0,0,20,39,45,
        52,59,63,73,85,91,104,110,128,139,147,152,160,184,192,194,202,216
    ]

class PyLiteParser ( Parser ):

    grammarFileName = "PyLiteParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'False'", "'await'", 
                     "'else'", "'import'", "'pass'", "'None'", "'break'", 
                     "'except'", "'in'", "'raise'", "'True'", "'class'", 
                     "'finally'", "'is'", "'return'", "'and'", "'continue'", 
                     "'for'", "'lambda'", "'try'", "'as'", "'def'", "'from'", 
                     "'nonlocal'", "'while'", "'assert'", "'del'", "'global'", 
                     "'not'", "'with'", "'async'", "'elif'", "'if'", "'or'", 
                     "'yield'", "'+'", "'-'", "'*'", "'**'", "'/'", "'//'", 
                     "'%'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'//='", "'%='", 
                     "'**='", "'&='", "'|='", "'^='", "'>>='", "'<<='", 
                     "':='", "'&'", "'|'", "'^'", "'~'", "'<<'", "'>>'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "':'", 
                     "'.'", "';'", "'@'", "'->'", "'...'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "FALSE", "AWAIT", 
                      "ELSE", "IMPORT", "PASS", "NONE", "BREAK", "EXCEPT", 
                      "IN", "RAISE", "TRUE", "CLASS", "FINALLY", "IS", "RETURN", 
                      "AND", "CONTINUE", "FOR", "LAMBDA", "TRY", "AS", "DEF", 
                      "FROM", "NONLOCAL", "WHILE", "ASSERT", "DEL", "GLOBAL", 
                      "NOT", "WITH", "ASYNC", "ELIF", "IF", "OR", "YIELD", 
                      "PLUS", "MINUS", "STAR", "DOUBLESTAR", "SLASH", "DOUBLESLASH", 
                      "PERCENT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "ASSIGN", 
                      "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", 
                      "DSLASH_ASSIGN", "PERCENT_ASSIGN", "POWER_ASSIGN", 
                      "AMP_ASSIGN", "PIPE_ASSIGN", "CARET_ASSIGN", "RSHIFT_ASSIGN", 
                      "LSHIFT_ASSIGN", "WALRUS", "AMP", "PIPE", "CARET", 
                      "TILDE", "LSHIFT", "RSHIFT", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "LBRACE", "RBRACE", "COMMA", "COLON", 
                      "DOT", "SEMI", "AT", "ARROW", "ELLIPSIS", "NAME", 
                      "INT", "FLOAT", "STRING", "COMMENT", "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_simpleStmt = 2
    RULE_smallStmt = 3
    RULE_assignStmt = 4
    RULE_assignOp = 5
    RULE_exprStmt = 6
    RULE_returnStmt = 7
    RULE_compoundStmt = 8
    RULE_ifStmt = 9
    RULE_whileStmt = 10
    RULE_forStmt = 11
    RULE_funcDef = 12
    RULE_paramList = 13
    RULE_block = 14
    RULE_expr = 15
    RULE_argList = 16
    RULE_atom = 17

    ruleNames =  [ "program", "statement", "simpleStmt", "smallStmt", "assignStmt", 
                   "assignOp", "exprStmt", "returnStmt", "compoundStmt", 
                   "ifStmt", "whileStmt", "forStmt", "funcDef", "paramList", 
                   "block", "expr", "argList", "atom" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    FALSE=3
    AWAIT=4
    ELSE=5
    IMPORT=6
    PASS=7
    NONE=8
    BREAK=9
    EXCEPT=10
    IN=11
    RAISE=12
    TRUE=13
    CLASS=14
    FINALLY=15
    IS=16
    RETURN=17
    AND=18
    CONTINUE=19
    FOR=20
    LAMBDA=21
    TRY=22
    AS=23
    DEF=24
    FROM=25
    NONLOCAL=26
    WHILE=27
    ASSERT=28
    DEL=29
    GLOBAL=30
    NOT=31
    WITH=32
    ASYNC=33
    ELIF=34
    IF=35
    OR=36
    YIELD=37
    PLUS=38
    MINUS=39
    STAR=40
    DOUBLESTAR=41
    SLASH=42
    DOUBLESLASH=43
    PERCENT=44
    EQ=45
    NEQ=46
    LE=47
    GE=48
    LT=49
    GT=50
    ASSIGN=51
    PLUS_ASSIGN=52
    MINUS_ASSIGN=53
    STAR_ASSIGN=54
    SLASH_ASSIGN=55
    DSLASH_ASSIGN=56
    PERCENT_ASSIGN=57
    POWER_ASSIGN=58
    AMP_ASSIGN=59
    PIPE_ASSIGN=60
    CARET_ASSIGN=61
    RSHIFT_ASSIGN=62
    LSHIFT_ASSIGN=63
    WALRUS=64
    AMP=65
    PIPE=66
    CARET=67
    TILDE=68
    LSHIFT=69
    RSHIFT=70
    LPAREN=71
    RPAREN=72
    LBRACKET=73
    RBRACKET=74
    LBRACE=75
    RBRACE=76
    COMMA=77
    COLON=78
    DOT=79
    SEMI=80
    AT=81
    ARROW=82
    ELLIPSIS=83
    NAME=84
    INT=85
    FLOAT=86
    STRING=87
    COMMENT=88
    WS=89
    NEWLINE=90

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PyLiteParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.NEWLINE)
            else:
                return self.getToken(PyLiteParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.StatementContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.StatementContext,i)


        def getRuleIndex(self):
            return PyLiteParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PyLiteParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 36
                self.match(PyLiteParser.NEWLINE)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 861293650824) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 122881) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(PyLiteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStmt(self):
            return self.getTypedRuleContext(PyLiteParser.SimpleStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(PyLiteParser.CompoundStmtContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PyLiteParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 7, 8, 9, 13, 17, 19, 31, 38, 39, 71, 84, 85, 86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.simpleStmt()
                pass
            elif token in [20, 24, 27, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.compoundStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def smallStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.SmallStmtContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.SmallStmtContext,i)


        def NEWLINE(self):
            return self.getToken(PyLiteParser.NEWLINE, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.SEMI)
            else:
                return self.getToken(PyLiteParser.SEMI, i)

        def getRuleIndex(self):
            return PyLiteParser.RULE_simpleStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = PyLiteParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.smallStmt()
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.match(PyLiteParser.SEMI)
                    self.state = 56
                    self.smallStmt() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 62
                self.match(PyLiteParser.SEMI)


            self.state = 65
            self.match(PyLiteParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(PyLiteParser.AssignStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(PyLiteParser.ExprStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(PyLiteParser.ReturnStmtContext,0)


        def PASS(self):
            return self.getToken(PyLiteParser.PASS, 0)

        def BREAK(self):
            return self.getToken(PyLiteParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(PyLiteParser.CONTINUE, 0)

        def getRuleIndex(self):
            return PyLiteParser.RULE_smallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmallStmt" ):
                return visitor.visitSmallStmt(self)
            else:
                return visitor.visitChildren(self)




    def smallStmt(self):

        localctx = PyLiteParser.SmallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_smallStmt)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.exprStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.returnStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(PyLiteParser.PASS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.match(PyLiteParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.match(PyLiteParser.CONTINUE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PyLiteParser.NAME, 0)

        def assignOp(self):
            return self.getTypedRuleContext(PyLiteParser.AssignOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = PyLiteParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PyLiteParser.NAME)
            self.state = 76
            self.assignOp()
            self.state = 77
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(PyLiteParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(PyLiteParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(PyLiteParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(PyLiteParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(PyLiteParser.SLASH_ASSIGN, 0)

        def getRuleIndex(self):
            return PyLiteParser.RULE_assignOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOp" ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = PyLiteParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69805794224242688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_exprStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = PyLiteParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PyLiteParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = PyLiteParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PyLiteParser.RETURN)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 826781212936) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 122881) != 0):
                self.state = 84
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(PyLiteParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(PyLiteParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(PyLiteParser.ForStmtContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(PyLiteParser.FuncDefContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_compoundStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStmt" ):
                return visitor.visitCompoundStmt(self)
            else:
                return visitor.visitChildren(self)




    def compoundStmt(self):

        localctx = PyLiteParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundStmt)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.ifStmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.whileStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.forStmt()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.funcDef()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PyLiteParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.COLON)
            else:
                return self.getToken(PyLiteParser.COLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.BlockContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.ELIF)
            else:
                return self.getToken(PyLiteParser.ELIF, i)

        def ELSE(self):
            return self.getToken(PyLiteParser.ELSE, 0)

        def getRuleIndex(self):
            return PyLiteParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = PyLiteParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(PyLiteParser.IF)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(PyLiteParser.COLON)
            self.state = 96
            self.block()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 97
                self.match(PyLiteParser.ELIF)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(PyLiteParser.COLON)
                self.state = 100
                self.block()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 107
                self.match(PyLiteParser.ELSE)
                self.state = 108
                self.match(PyLiteParser.COLON)
                self.state = 109
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PyLiteParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def COLON(self):
            return self.getToken(PyLiteParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(PyLiteParser.BlockContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = PyLiteParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PyLiteParser.WHILE)
            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(PyLiteParser.COLON)
            self.state = 115
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PyLiteParser.FOR, 0)

        def NAME(self):
            return self.getToken(PyLiteParser.NAME, 0)

        def IN(self):
            return self.getToken(PyLiteParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def COLON(self):
            return self.getToken(PyLiteParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(PyLiteParser.BlockContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = PyLiteParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PyLiteParser.FOR)
            self.state = 118
            self.match(PyLiteParser.NAME)
            self.state = 119
            self.match(PyLiteParser.IN)
            self.state = 120
            self.expr(0)
            self.state = 121
            self.match(PyLiteParser.COLON)
            self.state = 122
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(PyLiteParser.DEF, 0)

        def NAME(self):
            return self.getToken(PyLiteParser.NAME, 0)

        def LPAREN(self):
            return self.getToken(PyLiteParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PyLiteParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(PyLiteParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(PyLiteParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(PyLiteParser.ParamListContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_funcDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = PyLiteParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(PyLiteParser.DEF)
            self.state = 125
            self.match(PyLiteParser.NAME)
            self.state = 126
            self.match(PyLiteParser.LPAREN)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==84:
                self.state = 127
                self.paramList()


            self.state = 130
            self.match(PyLiteParser.RPAREN)
            self.state = 131
            self.match(PyLiteParser.COLON)
            self.state = 132
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.NAME)
            else:
                return self.getToken(PyLiteParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.COMMA)
            else:
                return self.getToken(PyLiteParser.COMMA, i)

        def getRuleIndex(self):
            return PyLiteParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = PyLiteParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(PyLiteParser.NAME)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==77:
                self.state = 135
                self.match(PyLiteParser.COMMA)
                self.state = 136
                self.match(PyLiteParser.NAME)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(PyLiteParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(PyLiteParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(PyLiteParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.StatementContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.StatementContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(PyLiteParser.SimpleStmtContext,0)


        def getRuleIndex(self):
            return PyLiteParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PyLiteParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [90]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(PyLiteParser.NEWLINE)
                self.state = 143
                self.match(PyLiteParser.INDENT)
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 144
                    self.statement()
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 861293650824) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 122881) != 0)):
                        break

                self.state = 149
                self.match(PyLiteParser.DEDENT)
                pass
            elif token in [3, 7, 8, 9, 13, 17, 19, 31, 38, 39, 71, 84, 85, 86, 87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.simpleStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PyLiteParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IndexExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def LBRACKET(self):
            return self.getToken(PyLiteParser.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(PyLiteParser.RBRACKET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(PyLiteParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(PyLiteParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PyLiteParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.STAR)
            else:
                return self.getToken(PyLiteParser.STAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(PyLiteParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(PyLiteParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def STAR(self):
            return self.getToken(PyLiteParser.STAR, 0)
        def SLASH(self):
            return self.getToken(PyLiteParser.SLASH, 0)
        def DOUBLESLASH(self):
            return self.getToken(PyLiteParser.DOUBLESLASH, 0)
        def PERCENT(self):
            return self.getToken(PyLiteParser.PERCENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PyLiteParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def OR(self):
            return self.getToken(PyLiteParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)

        def LPAREN(self):
            return self.getToken(PyLiteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(PyLiteParser.RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(PyLiteParser.ArgListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def EQ(self):
            return self.getToken(PyLiteParser.EQ, 0)
        def NEQ(self):
            return self.getToken(PyLiteParser.NEQ, 0)
        def LT(self):
            return self.getToken(PyLiteParser.LT, 0)
        def GT(self):
            return self.getToken(PyLiteParser.GT, 0)
        def LE(self):
            return self.getToken(PyLiteParser.LE, 0)
        def GE(self):
            return self.getToken(PyLiteParser.GE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)

        def AND(self):
            return self.getToken(PyLiteParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PyLiteParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 39]:
                localctx = PyLiteParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 155
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.expr(8)
                pass
            elif token in [31]:
                localctx = PyLiteParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(PyLiteParser.NOT)
                self.state = 158
                self.expr(4)
                pass
            elif token in [3, 8, 13, 71, 84, 85, 86, 87]:
                localctx = PyLiteParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = PyLiteParser.PowerExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 163
                        self.match(PyLiteParser.STAR)
                        self.state = 164
                        self.match(PyLiteParser.STAR)
                        self.state = 165
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PyLiteParser.MulExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 167
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31885837205504) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = PyLiteParser.AddExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 170
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==39):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 171
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = PyLiteParser.CompareExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 173
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2216615441596416) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = PyLiteParser.AndExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 175
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 176
                        self.match(PyLiteParser.AND)
                        self.state = 177
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = PyLiteParser.OrExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 178
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 179
                        self.match(PyLiteParser.OR)
                        self.state = 180
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = PyLiteParser.CallExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 182
                        self.match(PyLiteParser.LPAREN)
                        self.state = 184
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 826781212936) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 122881) != 0):
                            self.state = 183
                            self.argList()


                        self.state = 186
                        self.match(PyLiteParser.RPAREN)
                        pass

                    elif la_ == 8:
                        localctx = PyLiteParser.IndexExprContext(self, PyLiteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 188
                        self.match(PyLiteParser.LBRACKET)
                        self.state = 189
                        self.expr(0)
                        self.state = 190
                        self.match(PyLiteParser.RBRACKET)
                        pass

             
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyLiteParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PyLiteParser.COMMA)
            else:
                return self.getToken(PyLiteParser.COMMA, i)

        def getRuleIndex(self):
            return PyLiteParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = PyLiteParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expr(0)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==77:
                self.state = 198
                self.match(PyLiteParser.COMMA)
                self.state = 199
                self.expr(0)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PyLiteParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NameAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(PyLiteParser.NAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameAtom" ):
                return visitor.visitNameAtom(self)
            else:
                return visitor.visitChildren(self)


    class NoneAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NONE(self):
            return self.getToken(PyLiteParser.NONE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoneAtom" ):
                return visitor.visitNoneAtom(self)
            else:
                return visitor.visitChildren(self)


    class FloatAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PyLiteParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatAtom" ):
                return visitor.visitFloatAtom(self)
            else:
                return visitor.visitChildren(self)


    class ParenAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PyLiteParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(PyLiteParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(PyLiteParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenAtom" ):
                return visitor.visitParenAtom(self)
            else:
                return visitor.visitChildren(self)


    class IntAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PyLiteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntAtom" ):
                return visitor.visitIntAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PyLiteParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringAtom" ):
                return visitor.visitStringAtom(self)
            else:
                return visitor.visitChildren(self)


    class FalseAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(PyLiteParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseAtom" ):
                return visitor.visitFalseAtom(self)
            else:
                return visitor.visitChildren(self)


    class TrueAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyLiteParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(PyLiteParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueAtom" ):
                return visitor.visitTrueAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = PyLiteParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atom)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [84]:
                localctx = PyLiteParser.NameAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(PyLiteParser.NAME)
                pass
            elif token in [85]:
                localctx = PyLiteParser.IntAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(PyLiteParser.INT)
                pass
            elif token in [86]:
                localctx = PyLiteParser.FloatAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(PyLiteParser.FLOAT)
                pass
            elif token in [87]:
                localctx = PyLiteParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.match(PyLiteParser.STRING)
                pass
            elif token in [13]:
                localctx = PyLiteParser.TrueAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(PyLiteParser.TRUE)
                pass
            elif token in [3]:
                localctx = PyLiteParser.FalseAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 210
                self.match(PyLiteParser.FALSE)
                pass
            elif token in [8]:
                localctx = PyLiteParser.NoneAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 211
                self.match(PyLiteParser.NONE)
                pass
            elif token in [71]:
                localctx = PyLiteParser.ParenAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 212
                self.match(PyLiteParser.LPAREN)
                self.state = 213
                self.expr(0)
                self.state = 214
                self.match(PyLiteParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         




