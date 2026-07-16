# Generated from PyLiteParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PyLiteParser import PyLiteParser
else:
    from PyLiteParser import PyLiteParser

# This class defines a complete generic visitor for a parse tree produced by PyLiteParser.

class PyLiteParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PyLiteParser#program.
    def visitProgram(self, ctx:PyLiteParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#statement.
    def visitStatement(self, ctx:PyLiteParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#simpleStmt.
    def visitSimpleStmt(self, ctx:PyLiteParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#smallStmt.
    def visitSmallStmt(self, ctx:PyLiteParser.SmallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#assignStmt.
    def visitAssignStmt(self, ctx:PyLiteParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#assignOp.
    def visitAssignOp(self, ctx:PyLiteParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#exprStmt.
    def visitExprStmt(self, ctx:PyLiteParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#returnStmt.
    def visitReturnStmt(self, ctx:PyLiteParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#compoundStmt.
    def visitCompoundStmt(self, ctx:PyLiteParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#ifStmt.
    def visitIfStmt(self, ctx:PyLiteParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#whileStmt.
    def visitWhileStmt(self, ctx:PyLiteParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#forStmt.
    def visitForStmt(self, ctx:PyLiteParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#funcDef.
    def visitFuncDef(self, ctx:PyLiteParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#paramList.
    def visitParamList(self, ctx:PyLiteParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#block.
    def visitBlock(self, ctx:PyLiteParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#indexExpr.
    def visitIndexExpr(self, ctx:PyLiteParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#unaryExpr.
    def visitUnaryExpr(self, ctx:PyLiteParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#notExpr.
    def visitNotExpr(self, ctx:PyLiteParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#powerExpr.
    def visitPowerExpr(self, ctx:PyLiteParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#addExpr.
    def visitAddExpr(self, ctx:PyLiteParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#mulExpr.
    def visitMulExpr(self, ctx:PyLiteParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#atomExpr.
    def visitAtomExpr(self, ctx:PyLiteParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#orExpr.
    def visitOrExpr(self, ctx:PyLiteParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#callExpr.
    def visitCallExpr(self, ctx:PyLiteParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#compareExpr.
    def visitCompareExpr(self, ctx:PyLiteParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#andExpr.
    def visitAndExpr(self, ctx:PyLiteParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#argList.
    def visitArgList(self, ctx:PyLiteParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#nameAtom.
    def visitNameAtom(self, ctx:PyLiteParser.NameAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#intAtom.
    def visitIntAtom(self, ctx:PyLiteParser.IntAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#floatAtom.
    def visitFloatAtom(self, ctx:PyLiteParser.FloatAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#stringAtom.
    def visitStringAtom(self, ctx:PyLiteParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#trueAtom.
    def visitTrueAtom(self, ctx:PyLiteParser.TrueAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#falseAtom.
    def visitFalseAtom(self, ctx:PyLiteParser.FalseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#noneAtom.
    def visitNoneAtom(self, ctx:PyLiteParser.NoneAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLiteParser#parenAtom.
    def visitParenAtom(self, ctx:PyLiteParser.ParenAtomContext):
        return self.visitChildren(ctx)



del PyLiteParser