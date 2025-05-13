# Generated from logicEx.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logicExParser import logicExParser
else:
    from logicExParser import logicExParser

# This class defines a complete listener for a parse tree produced by logicExParser.
class logicExListener(ParseTreeListener):

    # Enter a parse tree produced by logicExParser#expression.
    def enterExpression(self, ctx:logicExParser.ExpressionContext):
        pass

    # Exit a parse tree produced by logicExParser#expression.
    def exitExpression(self, ctx:logicExParser.ExpressionContext):
        pass


    # Enter a parse tree produced by logicExParser#term.
    def enterTerm(self, ctx:logicExParser.TermContext):
        pass

    # Exit a parse tree produced by logicExParser#term.
    def exitTerm(self, ctx:logicExParser.TermContext):
        pass


    # Enter a parse tree produced by logicExParser#factor.
    def enterFactor(self, ctx:logicExParser.FactorContext):
        pass

    # Exit a parse tree produced by logicExParser#factor.
    def exitFactor(self, ctx:logicExParser.FactorContext):
        pass



del logicExParser