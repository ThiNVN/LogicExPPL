# Generated from PropositionalLogic.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("?\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\5\5#\n\5\3\6\3\6\3\6\5\6(\n\6")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\7\t\60\n\t\f\t\16\t\63\13\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\6\f:\n\f\r\f\16\f;\3\f\3\f\2\2\r")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3")
        buf.write("\2\7\4\2##\u0080\u0080\4\2--~~\4\2C\\c|\5\2C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\2B\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3")
        buf.write("\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t\"\3\2\2\2\13\'\3\2")
        buf.write("\2\2\r)\3\2\2\2\17+\3\2\2\2\21-\3\2\2\2\23\64\3\2\2\2")
        buf.write("\25\66\3\2\2\2\279\3\2\2\2\31\32\t\2\2\2\32\4\3\2\2\2")
        buf.write("\33\34\7(\2\2\34\6\3\2\2\2\35\36\t\3\2\2\36\b\3\2\2\2")
        buf.write("\37#\7`\2\2 !\7#\2\2!#\7(\2\2\"\37\3\2\2\2\" \3\2\2\2")
        buf.write("#\n\3\2\2\2$(\7,\2\2%&\7#\2\2&(\7-\2\2\'$\3\2\2\2\'%\3")
        buf.write("\2\2\2(\f\3\2\2\2)*\7\63\2\2*\16\3\2\2\2+,\7\62\2\2,\20")
        buf.write("\3\2\2\2-\61\t\4\2\2.\60\t\5\2\2/.\3\2\2\2\60\63\3\2\2")
        buf.write("\2\61/\3\2\2\2\61\62\3\2\2\2\62\22\3\2\2\2\63\61\3\2\2")
        buf.write("\2\64\65\7*\2\2\65\24\3\2\2\2\66\67\7+\2\2\67\26\3\2\2")
        buf.write("\28:\t\6\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<")
        buf.write("=\3\2\2\2=>\b\f\2\2>\30\3\2\2\2\7\2\"\'\61;\3\b\2\2")
        return buf.getvalue()


class PropositionalLogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NOT = 1
    AND = 2
    OR = 3
    NAND = 4
    NOR = 5
    TRUE = 6
    FALSE = 7
    ID = 8
    LPAREN = 9
    RPAREN = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'&'", "'1'", "'0'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NOT", "AND", "OR", "NAND", "NOR", "TRUE", "FALSE", "ID", "LPAREN", 
            "RPAREN", "WS" ]

    ruleNames = [ "NOT", "AND", "OR", "NAND", "NOR", "TRUE", "FALSE", "ID", 
                  "LPAREN", "RPAREN", "WS" ]

    grammarFileName = "PropositionalLogic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


