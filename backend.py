import itertools
from antlr4 import *
from CompiledFiles.PropositionalLogicLexer import PropositionalLogicLexer
from CompiledFiles.PropositionalLogicParser import PropositionalLogicParser
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error at line {line}, column {column}: {msg}")

def parse_and_evaluate(expr, assignments):
    input_stream = InputStream(expr)
    lexer = PropositionalLogicLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PropositionalLogicParser(token_stream)
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.expression()
    if error_listener.errors:
        raise Exception("Parse error: " + ", ".join(error_listener.errors))
    return evaluate_tree(tree, assignments)

def evaluate_tree(tree, assignments):
    if tree.getChildCount() == 0:
        text = tree.getText()
        if text == '1':
            return True
        elif text == '0':
            return False
        elif text in assignments:
            return assignments[text]
        else:
            raise ValueError(f"Undefined variable: {text}")

    rule_name = tree.getRuleContext().__class__.__name__
    
    if rule_name == 'UnaryExpressionContext':
        return not evaluate_tree(tree.getChild(1), assignments)
    elif rule_name == 'BinaryExpressionContext':
        left = evaluate_tree(tree.getChild(0), assignments)
        op = tree.getChild(1).getText()
        right = evaluate_tree(tree.getChild(2), assignments)
        
        if op in ['&']:  # AND
            return left and right
        elif op in ['|', '+']:  # OR
            return left or right
        elif op in ['^']:  # XOR
            return (left and not right) or (not left and right)
        elif op in ['!&']:  # NAND
            return not (left and right)
        elif op in ['*', '!+']:  # NOR
            return not (left or right)
    elif rule_name == 'ParenthesizedExpressionContext':
        return evaluate_tree(tree.getChild(1), assignments)
    elif rule_name == 'AtomExpressionContext':
        return evaluate_tree(tree.getChild(0), assignments)
    elif rule_name == 'AtomContext':
        text = tree.getText()
        if text == '1':
            return True
        elif text == '0':
            return False
        elif text in assignments:
            return assignments[text]
        else:
            raise ValueError(f"Undefined variable: {text}")
    
    raise ValueError(f"Unknown expression type: {rule_name}")

def generate_truth_table(expr):
    variables = sorted(set([c for c in expr if c.isalpha()]))
    if not variables:
        raise Exception("No variables found in expression.")
    combos = list(itertools.product([1, 0], repeat=len(variables)))
    results = []
    for vals in combos:
        assignments = {var: bool(val) for var, val in zip(variables, vals)}
        try:
            result = parse_and_evaluate(expr, assignments)
        except Exception as e:
            raise e
        results.append(list(vals) + [int(result)])
    return variables, results 

def check_grammar(expr):
    input_stream = InputStream(expr)
    lexer = PropositionalLogicLexer(input_stream)
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    token_stream = CommonTokenStream(lexer)
    parser = PropositionalLogicParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    parser.expression()
    if error_listener.errors:
        return False, ", ".join(error_listener.errors)
    return True, None 