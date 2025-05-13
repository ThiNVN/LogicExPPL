# Generated from logicEx.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("$\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write("\5\4\32\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\4\2\2")
        buf.write("\5\2\4\6\2\2\2%\2\b\3\2\2\2\4\20\3\2\2\2\6\31\3\2\2\2")
        buf.write("\b\r\5\4\3\2\t\n\7\4\2\2\n\f\5\4\3\2\13\t\3\2\2\2\f\17")
        buf.write("\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\r\3")
        buf.write("\2\2\2\20\25\5\6\4\2\21\22\7\3\2\2\22\24\5\6\4\2\23\21")
        buf.write("\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\5\3\2\2\2\27\25\3\2\2\2\30\32\7\5\2\2\31\30\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32!\3\2\2\2\33\34\7\6\2\2\34\35\5\2\2\2\35")
        buf.write("\36\7\7\2\2\36\"\3\2\2\2\37\"\7\b\2\2 \"\7\t\2\2!\33\3")
        buf.write("\2\2\2!\37\3\2\2\2! \3\2\2\2\"\7\3\2\2\2\6\r\25\31!")
        return buf.getvalue()


class logicExParser ( Parser ):

    grammarFileName = "logicEx.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "LPAREN", "RPAREN", 
                      "IDENTIFIER", "BOOL", "WS" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expression", "term", "factor" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    LPAREN=4
    RPAREN=5
    IDENTIFIER=6
    BOOL=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logicExParser.TermContext)
            else:
                return self.getTypedRuleContext(logicExParser.TermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(logicExParser.OR)
            else:
                return self.getToken(logicExParser.OR, i)

        def getRuleIndex(self):
            return logicExParser.RULE_expression




    def expression(self):

        localctx = logicExParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.term()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==logicExParser.OR:
                self.state = 7
                self.match(logicExParser.OR)
                self.state = 8
                self.term()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logicExParser.FactorContext)
            else:
                return self.getTypedRuleContext(logicExParser.FactorContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(logicExParser.AND)
            else:
                return self.getToken(logicExParser.AND, i)

        def getRuleIndex(self):
            return logicExParser.RULE_term




    def term(self):

        localctx = logicExParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.factor()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==logicExParser.AND:
                self.state = 15
                self.match(logicExParser.AND)
                self.state = 16
                self.factor()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(logicExParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(logicExParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(logicExParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(logicExParser.IDENTIFIER, 0)

        def BOOL(self):
            return self.getToken(logicExParser.BOOL, 0)

        def NOT(self):
            return self.getToken(logicExParser.NOT, 0)

        def getRuleIndex(self):
            return logicExParser.RULE_factor




    def factor(self):

        localctx = logicExParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==logicExParser.NOT:
                self.state = 22
                self.match(logicExParser.NOT)


            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [logicExParser.LPAREN]:
                self.state = 25
                self.match(logicExParser.LPAREN)
                self.state = 26
                self.expression()
                self.state = 27
                self.match(logicExParser.RPAREN)
                pass
            elif token in [logicExParser.IDENTIFIER]:
                self.state = 29
                self.match(logicExParser.IDENTIFIER)
                pass
            elif token in [logicExParser.BOOL]:
                self.state = 30
                self.match(logicExParser.BOOL)
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





