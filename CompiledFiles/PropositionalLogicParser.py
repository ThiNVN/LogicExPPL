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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("9\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\64\n\3\f")
        buf.write("\3\16\3\67\13\3\3\3\2\3\4\4\2\4\2\2\2D\2\6\3\2\2\2\4\23")
        buf.write("\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\b\3\1")
        buf.write("\2\n\13\7\3\2\2\13\24\5\4\3\21\f\r\7\n\2\2\r\16\5\4\3")
        buf.write("\2\16\17\7\13\2\2\17\24\3\2\2\2\20\24\7\f\2\2\21\24\7")
        buf.write("\b\2\2\22\24\7\t\2\2\23\t\3\2\2\2\23\f\3\2\2\2\23\20\3")
        buf.write("\2\2\2\23\21\3\2\2\2\23\22\3\2\2\2\24\65\3\2\2\2\25\26")
        buf.write("\f\20\2\2\26\27\7\4\2\2\27\64\5\4\3\21\30\31\f\17\2\2")
        buf.write("\31\32\7\5\2\2\32\64\5\4\3\20\33\34\f\16\2\2\34\35\7\6")
        buf.write("\2\2\35\64\5\4\3\17\36\37\f\r\2\2\37 \7\7\2\2 \64\5\4")
        buf.write("\3\16!\"\f\f\2\2\"#\7\16\2\2#\64\5\4\3\r$%\f\13\2\2%&")
        buf.write("\7\17\2\2&\64\5\4\3\f\'(\f\n\2\2()\7\20\2\2)\64\5\4\3")
        buf.write("\13*+\f\t\2\2+,\7\21\2\2,\64\5\4\3\n-.\f\b\2\2./\7\22")
        buf.write("\2\2/\64\5\4\3\t\60\61\f\7\2\2\61\62\7\23\2\2\62\64\5")
        buf.write("\4\3\b\63\25\3\2\2\2\63\30\3\2\2\2\63\33\3\2\2\2\63\36")
        buf.write("\3\2\2\2\63!\3\2\2\2\63$\3\2\2\2\63\'\3\2\2\2\63*\3\2")
        buf.write("\2\2\63-\3\2\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2")
        buf.write("\2\2\65\66\3\2\2\2\66\5\3\2\2\2\67\65\3\2\2\2\5\23\63")
        buf.write("\65")
        return buf.getvalue()


class PropositionalLogicParser ( Parser ):

    grammarFileName = "PropositionalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NOT", "AND", "OR", "IMPLIES", "IFF", 
                      "TRUE", "FALSE", "LPAREN", "RPAREN", "IDENTIFIER", 
                      "WS", "NAND", "NOR", "XOR", "LEFTIMPLIES", "NIMPLIES", 
                      "LNIMPLIES" ]

    RULE_program = 0
    RULE_expression = 1

    ruleNames =  [ "program", "expression" ]

    EOF = Token.EOF
    NOT=1
    AND=2
    OR=3
    IMPLIES=4
    IFF=5
    TRUE=6
    FALSE=7
    LPAREN=8
    RPAREN=9
    IDENTIFIER=10
    WS=11
    NAND=12
    NOR=13
    XOR=14
    LEFTIMPLIES=15
    NIMPLIES=16
    LNIMPLIES=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(PropositionalLogicParser.EOF, 0)

        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_program




    def program(self):

        localctx = PropositionalLogicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expression(0)
            self.state = 5
            self.match(PropositionalLogicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PropositionalLogicParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(PropositionalLogicParser.AND, 0)


    class TrueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(PropositionalLogicParser.TRUE, 0)


    class ImpliesExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def IMPLIES(self):
            return self.getToken(PropositionalLogicParser.IMPLIES, 0)


    class XorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def XOR(self):
            return self.getToken(PropositionalLogicParser.XOR, 0)


    class LeftImpliesExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def LEFTIMPLIES(self):
            return self.getToken(PropositionalLogicParser.LEFTIMPLIES, 0)


    class LNImpliesExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def LNIMPLIES(self):
            return self.getToken(PropositionalLogicParser.LNIMPLIES, 0)


    class IffExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def IFF(self):
            return self.getToken(PropositionalLogicParser.IFF, 0)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(PropositionalLogicParser.OR, 0)


    class FalseExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(PropositionalLogicParser.FALSE, 0)


    class NandExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def NAND(self):
            return self.getToken(PropositionalLogicParser.NAND, 0)


    class NorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def NOR(self):
            return self.getToken(PropositionalLogicParser.NOR, 0)


    class IdentifierExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PropositionalLogicParser.IDENTIFIER, 0)


    class NImpliesExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropositionalLogicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,i)

        def NIMPLIES(self):
            return self.getToken(PropositionalLogicParser.NIMPLIES, 0)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PropositionalLogicParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,0)



    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PropositionalLogicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PropositionalLogicParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(PropositionalLogicParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(PropositionalLogicParser.RPAREN, 0)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PropositionalLogicParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PropositionalLogicParser.NOT]:
                localctx = PropositionalLogicParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(PropositionalLogicParser.NOT)
                self.state = 9
                self.expression(15)
                pass
            elif token in [PropositionalLogicParser.LPAREN]:
                localctx = PropositionalLogicParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(PropositionalLogicParser.LPAREN)
                self.state = 11
                self.expression(0)
                self.state = 12
                self.match(PropositionalLogicParser.RPAREN)
                pass
            elif token in [PropositionalLogicParser.IDENTIFIER]:
                localctx = PropositionalLogicParser.IdentifierExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(PropositionalLogicParser.IDENTIFIER)
                pass
            elif token in [PropositionalLogicParser.TRUE]:
                localctx = PropositionalLogicParser.TrueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(PropositionalLogicParser.TRUE)
                pass
            elif token in [PropositionalLogicParser.FALSE]:
                localctx = PropositionalLogicParser.FalseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(PropositionalLogicParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PropositionalLogicParser.AndExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 19
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 20
                        self.match(PropositionalLogicParser.AND)
                        self.state = 21
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = PropositionalLogicParser.OrExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 22
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 23
                        self.match(PropositionalLogicParser.OR)
                        self.state = 24
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = PropositionalLogicParser.ImpliesExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 26
                        self.match(PropositionalLogicParser.IMPLIES)
                        self.state = 27
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = PropositionalLogicParser.IffExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 29
                        self.match(PropositionalLogicParser.IFF)
                        self.state = 30
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = PropositionalLogicParser.NandExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 32
                        self.match(PropositionalLogicParser.NAND)
                        self.state = 33
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = PropositionalLogicParser.NorExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 35
                        self.match(PropositionalLogicParser.NOR)
                        self.state = 36
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = PropositionalLogicParser.XorExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 37
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 38
                        self.match(PropositionalLogicParser.XOR)
                        self.state = 39
                        self.expression(9)
                        pass

                    elif la_ == 8:
                        localctx = PropositionalLogicParser.LeftImpliesExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 41
                        self.match(PropositionalLogicParser.LEFTIMPLIES)
                        self.state = 42
                        self.expression(8)
                        pass

                    elif la_ == 9:
                        localctx = PropositionalLogicParser.NImpliesExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 44
                        self.match(PropositionalLogicParser.NIMPLIES)
                        self.state = 45
                        self.expression(7)
                        pass

                    elif la_ == 10:
                        localctx = PropositionalLogicParser.LNImpliesExprContext(self, PropositionalLogicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 47
                        self.match(PropositionalLogicParser.LNIMPLIES)
                        self.state = 48
                        self.expression(6)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         




