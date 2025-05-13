from antlr4 import *
from CompiledFiles.logicExLexer import logicExLexer
from CompiledFiles.logicExParser import logicExParser
from CompiledFiles.logicExListener import logicExListener
import itertools
import os

class LogicExpressionError(Exception):
    pass

class LogicExpressionListener(logicExListener):
    def __init__(self, variables):
        self.variables = variables
        self.result = None

    def enterExpression(self, ctx):
        if len(ctx.term()) == 1:
            self.result = self.visit(ctx.term(0))
        else:
            result = self.visit(ctx.term(0))
            for i in range(1, len(ctx.term())):
                result = result or self.visit(ctx.term(i))
            self.result = result

    def enterTerm(self, ctx):
        if len(ctx.factor()) == 1:
            return self.visit(ctx.factor(0))
        else:
            result = self.visit(ctx.factor(0))
            for i in range(1, len(ctx.factor())):
                result = result and self.visit(ctx.factor(i))
            return result

    def enterFactor(self, ctx):
        if ctx.NOT():
            return not self.visit(ctx.expression() if ctx.expression() else ctx.IDENTIFIER() or ctx.BOOL())
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                raise LogicExpressionError(f"Variable {var_name} not found in variables")
            return self.variables[var_name]
        if ctx.BOOL():
            return ctx.BOOL().getText().lower() == 'true'
        return False

    def visit(self, node):
        if hasattr(node, 'accept'):
            return node.accept(self)
        return None

    def visitChildren(self, node):
        result = None
        for child in node.getChildren():
            child_result = self.visit(child)
            if child_result is not None:
                result = child_result
        return result

def check_grammar(expression):
    try:
        # Use InputStream directly with the expression string
        input_stream = InputStream(expression)
        lexer = logicExLexer(input_stream)
        tokens = []
        token = lexer.nextToken()
        while token.type != Token.EOF:
            tokens.append(token.text)
            token = lexer.nextToken()
        tokens.append('<EOF>')
        
        # Check if the expression is valid
        parser = logicExParser(CommonTokenStream(lexer))
        parser.expression()
        
        return True, f"Valid expression. Tokens: {', '.join(tokens)}"
    except Exception as e:
        return False, f"Invalid expression: {str(e)}"

def evaluate_expression(expression, variables):
    try:
        input_stream = InputStream(expression)
        lexer = logicExLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = logicExParser(stream)
        tree = parser.expression()
        listener = LogicExpressionListener(variables)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.result
    except Exception as e:
        raise LogicExpressionError(f"Error evaluating expression: {str(e)}")

def get_variables(expression):
    input_stream = InputStream(expression)
    lexer = logicExLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = logicExParser(stream)
    tree = parser.expression()
    
    variables = set()
    for token in stream.tokens:
        if token.type == logicExLexer.IDENTIFIER:
            variables.add(token.text)
    return sorted(list(variables))

def generate_truth_table(expression):
    try:
        variables = get_variables(expression)
        if not variables:
            return [], []
        
        # Generate all possible combinations of variable values
        combinations = list(itertools.product([False, True], repeat=len(variables)))
        
        # Calculate results for each combination
        results = []
        for combo in combinations:
            var_dict = dict(zip(variables, combo))
            try:
                result = evaluate_expression(expression, var_dict)
                results.append(list(combo) + [result])
            except LogicExpressionError as e:
                print(f"Error evaluating expression: {str(e)}")
                return [], []
        
        return variables, results
    except Exception as e:
        print(f"Error generating truth table: {str(e)}")
        return [], [] 