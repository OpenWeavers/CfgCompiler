# Generated from Cfg.g4 by ANTLR 4.7.1
from antlr4 import *
from collections import defaultdict

if __name__ is not None and "." in __name__:
    from .CfgParser import CfgParser
    from .CfgLexer import CfgLexer
    from .Cfg import Cfg
else:
    from CfgParser import CfgParser
    from CfgLexer import CfgLexer
    from Cfg import Cfg


# This class defines a complete generic visitor for a parse tree produced by CfgParser.

class CfgVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by CfgParser#prog.

    V = {}
    T = set()
    P = defaultdict(list)
    S = None

    gotS = False

    def __init__(self, stream):
        super().__init__()
        for token in stream.tokens:
            if token.type == CfgLexer.TERMINAL:
                self.T |= {token.text}
            elif token.type == CfgLexer.VARIABLE:
                self.V[token.text] = False

    def visitProg(self, ctx: CfgParser.ProgContext):
        for prod in ctx.production():
            self.visitProduction(prod)
        print(self.V, self.T, self.P, self.S, sep='\n')
        for v in self.V:
            if not self.V[v]:
                print("W: Undefined Variable %s" % v)
        return Cfg(set(self.V.keys()), self.T, self.P, self.S)

    # Visit a parse tree produced by CfgParser#production.
    def visitProduction(self, ctx: CfgParser.ProductionContext):
        # print("In Production %s" % ctx.getText())
        head = self.visitHead(ctx.head())
        for body in ctx.body():
            self.P[head].append(self.visitBody(body))

    # Visit a parse tree produced by CfgParser#head.
    def visitHead(self, ctx: CfgParser.HeadContext):
        if not self.gotS:
            self.S = ctx.getText()
            self.gotS = True
        self.V[ctx.getText()] = True
        return ctx.getText()

    # Visit a parse tree produced by CfgParser#body.
    def visitBody(self, ctx: CfgParser.BodyContext):
        res = []
        for ele in ctx.ele():
            res.append(self.visitEle(ele))
        return res

    # Visit a parse tree produced by CfgParser#ele.
    def visitEle(self, ctx: CfgParser.EleContext):
        return ctx.getText()


del CfgParser
