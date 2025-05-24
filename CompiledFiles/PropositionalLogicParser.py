# Generated from PropositionalLogic.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\2\3\2\3\2\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\2\3\2\6")
        buf.write("\2\4\6\b\2\4\3\2\4\7\3\2\b\n\2#\2\23\3\2\2\2\4\36\3\2")
        buf.write("\2\2\6 \3\2\2\2\b\"\3\2\2\2\n\13\b\2\1\2\13\f\5\6\4\2")
        buf.write("\f\r\5\2\2\5\r\24\3\2\2\2\16\24\5\b\5\2\17\20\7\13\2\2")
        buf.write("\20\21\5\2\2\2\21\22\7\f\2\2\22\24\3\2\2\2\23\n\3\2\2")
        buf.write("\2\23\16\3\2\2\2\23\17\3\2\2\2\24\33\3\2\2\2\25\26\f\6")
        buf.write("\2\2\26\27\5\4\3\2\27\30\5\2\2\7\30\32\3\2\2\2\31\25\3")
        buf.write("\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\3")
        buf.write("\3\2\2\2\35\33\3\2\2\2\36\37\t\2\2\2\37\5\3\2\2\2 !\7")
        buf.write("\3\2\2!\7\3\2\2\2\"#\t\3\2\2#\t\3\2\2\2\4\23\33")
        return buf.getvalue()


class PropositionalLogicParser ( Parser ):

    grammarFileName = "PropositionalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'&'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'1'", "'0'", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NOT", "AND", "OR", "NAND", "NOR", "TRUE", 
                      "FALSE", "ID", "LPAREN", "RPAREN", "WS" ]

    RULE_expression = 0
    RULE_binaryOp = 1
    RULE_unaryOp = 2
    RULE_atom = 3

    ruleNames =  [ "expression", "binaryOp", "unaryOp", "atom" ]

    EOF = Token.EOF
    NOT=1
    AND=2
    OR=3
    NAND=4
    NOR=5
    TRUE=6
    FALSE=7
    ID=8
    LPAREN=9
    RPAREN=10
    WS=11

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


        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesizedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PropositionalLogicParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(PropositionalLogicParser.RPAREN, 0)


    class BinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def binaryOp(self):
            return self.getTypedRuleContext(PropositionalLogicParser.BinaryOpContext,0)



    class UnaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryOp(self):
            return self.getTypedRuleContext(PropositionalLogicParser.UnaryOpContext,0)

        def expression(self):
            return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,0)



    class AtomExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PropositionalLogicParser.AtomContext,0)




    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropositionalLogicParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PropositionalLogicParser.NOT]:
                localctx = PropositionalLogicParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.unaryOp()
                self.state = 10
                self.expression(3)
                pass
            elif token in [PropositionalLogicParser.TRUE, PropositionalLogicParser.FALSE, PropositionalLogicParser.ID]:
                localctx = PropositionalLogicParser.AtomExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.atom()
                pass
            elif token in [PropositionalLogicParser.LPAREN]:
                localctx = PropositionalLogicParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(PropositionalLogicParser.LPAREN)
                self.state = 14
                self.expression(0)
                self.state = 15
                self.match(PropositionalLogicParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PropositionalLogicParser.BinaryExpressionContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 19
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 20
                    self.binaryOp()
                    self.state = 21
                    self.expression(5) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PropositionalLogicParser.AND, 0)

        def OR(self):
            return self.getToken(PropositionalLogicParser.OR, 0)

        def NAND(self):
            return self.getToken(PropositionalLogicParser.NAND, 0)

        def NOR(self):
            return self.getToken(PropositionalLogicParser.NOR, 0)

        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_binaryOp




    def binaryOp(self):

        localctx = PropositionalLogicParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PropositionalLogicParser.AND) | (1 << PropositionalLogicParser.OR) | (1 << PropositionalLogicParser.NAND) | (1 << PropositionalLogicParser.NOR))) != 0)):
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


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PropositionalLogicParser.NOT, 0)

        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_unaryOp




    def unaryOp(self):

        localctx = PropositionalLogicParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unaryOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(PropositionalLogicParser.NOT)
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

        def TRUE(self):
            return self.getToken(PropositionalLogicParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PropositionalLogicParser.FALSE, 0)

        def ID(self):
            return self.getToken(PropositionalLogicParser.ID, 0)

        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_atom




    def atom(self):

        localctx = PropositionalLogicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PropositionalLogicParser.TRUE) | (1 << PropositionalLogicParser.FALSE) | (1 << PropositionalLogicParser.ID))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




