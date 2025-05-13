# Generated from logicEx.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\35\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\7\7\67\n\7\f\7\16\7:\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bN\n\b")
        buf.write("\3\t\6\tQ\n\t\r\t\16\tR\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\3\2\5\4\2C\\c|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\2b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\3\34\3\2\2\2\5%\3\2\2\2\7.\3\2\2\2\t\60\3\2\2")
        buf.write("\2\13\62\3\2\2\2\r\64\3\2\2\2\17M\3\2\2\2\21P\3\2\2\2")
        buf.write("\23\24\7C\2\2\24\25\7P\2\2\25\35\7F\2\2\26\27\7c\2\2\27")
        buf.write("\30\7p\2\2\30\35\7f\2\2\31\32\7(\2\2\32\35\7(\2\2\33\35")
        buf.write("\7(\2\2\34\23\3\2\2\2\34\26\3\2\2\2\34\31\3\2\2\2\34\33")
        buf.write("\3\2\2\2\35\4\3\2\2\2\36\37\7Q\2\2\37&\7T\2\2 !\7q\2\2")
        buf.write("!&\7t\2\2\"#\7~\2\2#&\7~\2\2$&\7~\2\2%\36\3\2\2\2% \3")
        buf.write("\2\2\2%\"\3\2\2\2%$\3\2\2\2&\6\3\2\2\2\'(\7P\2\2()\7Q")
        buf.write("\2\2)/\7V\2\2*+\7p\2\2+,\7q\2\2,/\7v\2\2-/\7#\2\2.\'\3")
        buf.write("\2\2\2.*\3\2\2\2.-\3\2\2\2/\b\3\2\2\2\60\61\7*\2\2\61")
        buf.write("\n\3\2\2\2\62\63\7+\2\2\63\f\3\2\2\2\648\t\2\2\2\65\67")
        buf.write("\t\3\2\2\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29\16\3\2\2\2:8\3\2\2\2;<\7V\2\2<=\7T\2\2=>\7W\2\2>N")
        buf.write("\7G\2\2?@\7H\2\2@A\7C\2\2AB\7N\2\2BC\7U\2\2CN\7G\2\2D")
        buf.write("E\7v\2\2EF\7t\2\2FG\7w\2\2GN\7g\2\2HI\7h\2\2IJ\7c\2\2")
        buf.write("JK\7n\2\2KL\7u\2\2LN\7g\2\2M;\3\2\2\2M?\3\2\2\2MD\3\2")
        buf.write("\2\2MH\3\2\2\2N\20\3\2\2\2OQ\t\4\2\2PO\3\2\2\2QR\3\2\2")
        buf.write("\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\t\2\2U\22\3\2\2\2")
        buf.write("\t\2\34%.8MR\3\b\2\2")
        return buf.getvalue()


class logicExLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    OR = 2
    NOT = 3
    LPAREN = 4
    RPAREN = 5
    IDENTIFIER = 6
    BOOL = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "NOT", "LPAREN", "RPAREN", "IDENTIFIER", "BOOL", 
            "WS" ]

    ruleNames = [ "AND", "OR", "NOT", "LPAREN", "RPAREN", "IDENTIFIER", 
                  "BOOL", "WS" ]

    grammarFileName = "logicEx.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


