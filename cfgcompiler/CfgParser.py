# Generated from Cfg.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\6\2\21\n\2\r\2\16\2\22\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3\33\n\3\f\3\16\3\36\13\3\3\3\3\3\3\4\3\4\3\5\7\5%")
        buf.write("\n\5\f\5\16\5(\13\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3")
        buf.write("\2\b\t\2*\2\20\3\2\2\2\4\24\3\2\2\2\6!\3\2\2\2\b&\3\2")
        buf.write("\2\2\n)\3\2\2\2\f\16\5\4\3\2\r\17\7\3\2\2\16\r\3\2\2\2")
        buf.write("\16\17\3\2\2\2\17\21\3\2\2\2\20\f\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\20\3\2\2\2\22\23\3\2\2\2\23\3\3\2\2\2\24\25\5\6")
        buf.write("\4\2\25\26\7\4\2\2\26\27\7\5\2\2\27\34\5\b\5\2\30\31\7")
        buf.write("\6\2\2\31\33\5\b\5\2\32\30\3\2\2\2\33\36\3\2\2\2\34\32")
        buf.write("\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37")
        buf.write(" \7\7\2\2 \5\3\2\2\2!\"\7\b\2\2\"\7\3\2\2\2#%\5\n\6\2")
        buf.write("$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\t\3\2\2\2")
        buf.write("(&\3\2\2\2)*\t\2\2\2*\13\3\2\2\2\6\16\22\34&")
        return buf.getvalue()


class CfgParser ( Parser ):

    grammarFileName = "Cfg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "'-'", "'>'", "'|'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VARIABLE", "TERMINAL", 
                      "WS" ]

    RULE_prog = 0
    RULE_production = 1
    RULE_head = 2
    RULE_body = 3
    RULE_ele = 4

    ruleNames =  [ "prog", "production", "head", "body", "ele" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    VARIABLE=6
    TERMINAL=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def production(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CfgParser.ProductionContext)
            else:
                return self.getTypedRuleContext(CfgParser.ProductionContext,i)


        def getRuleIndex(self):
            return CfgParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CfgParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.production()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CfgParser.T__0:
                    self.state = 11
                    self.match(CfgParser.T__0)


                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CfgParser.VARIABLE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(CfgParser.HeadContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CfgParser.BodyContext)
            else:
                return self.getTypedRuleContext(CfgParser.BodyContext,i)


        def getRuleIndex(self):
            return CfgParser.RULE_production

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProduction" ):
                return visitor.visitProduction(self)
            else:
                return visitor.visitChildren(self)




    def production(self):

        localctx = CfgParser.ProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_production)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.head()
            self.state = 19
            self.match(CfgParser.T__1)
            self.state = 20
            self.match(CfgParser.T__2)
            self.state = 21
            self.body()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CfgParser.T__3:
                self.state = 22
                self.match(CfgParser.T__3)
                self.state = 23
                self.body()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(CfgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(CfgParser.VARIABLE, 0)

        def getRuleIndex(self):
            return CfgParser.RULE_head

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)




    def head(self):

        localctx = CfgParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_head)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CfgParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CfgParser.EleContext)
            else:
                return self.getTypedRuleContext(CfgParser.EleContext,i)


        def getRuleIndex(self):
            return CfgParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CfgParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CfgParser.VARIABLE or _la==CfgParser.TERMINAL:
                self.state = 33
                self.ele()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(CfgParser.VARIABLE, 0)

        def TERMINAL(self):
            return self.getToken(CfgParser.TERMINAL, 0)

        def getRuleIndex(self):
            return CfgParser.RULE_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle" ):
                return visitor.visitEle(self)
            else:
                return visitor.visitChildren(self)




    def ele(self):

        localctx = CfgParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ele)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==CfgParser.VARIABLE or _la==CfgParser.TERMINAL):
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





