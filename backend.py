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
    tree = parser.program()
    if error_listener.errors:
        raise Exception("Parse error: " + ", ".join(error_listener.errors))
    return evaluate_tree(tree, assignments)

def evaluate_tree(tree, assignments):
    if tree.getRuleContext().__class__.__name__ == 'ProgramContext':
        return evaluate_tree(tree.getChild(0), assignments)
    if tree.getChildCount() == 0:
        text = tree.getText()
        if text in ['true', 'True', 'TRUE']:
            return True
        elif text in ['false', 'False', 'FALSE']:
            return False
        elif text in assignments:
            return assignments[text]
        else:
            raise ValueError(f"Undefined variable: {text}")
    rule_name = tree.getRuleContext().__class__.__name__
    if rule_name == 'NotExprContext':
        return not evaluate_tree(tree.getChild(1), assignments)
    elif rule_name == 'AndExprContext':
        return evaluate_tree(tree.getChild(0), assignments) and evaluate_tree(tree.getChild(2), assignments)
    elif rule_name == 'OrExprContext':
        return evaluate_tree(tree.getChild(0), assignments) or evaluate_tree(tree.getChild(2), assignments)
    elif rule_name == 'ImpliesExprContext':
        return (not evaluate_tree(tree.getChild(0), assignments)) or evaluate_tree(tree.getChild(2), assignments)
    elif rule_name == 'IffExprContext':
        return evaluate_tree(tree.getChild(0), assignments) == evaluate_tree(tree.getChild(2), assignments)
    elif rule_name == 'ParenExprContext':
        return evaluate_tree(tree.getChild(1), assignments)
    elif rule_name == 'IdentifierExprContext':
        var = tree.getText()
        if var in assignments:
            return assignments[var]
        raise ValueError(f"Undefined variable: {var}")
    elif rule_name in ['TrueExprContext', 'FalseExprContext']:
        return rule_name == 'TrueExprContext'
    elif rule_name == 'NandExprContext':
        return not (evaluate_tree(tree.getChild(0), assignments) and evaluate_tree(tree.getChild(2), assignments))
    elif rule_name == 'NorExprContext':
        return not (evaluate_tree(tree.getChild(0), assignments) or evaluate_tree(tree.getChild(2), assignments))
    elif rule_name == 'XorExprContext':
        return evaluate_tree(tree.getChild(0), assignments) != evaluate_tree(tree.getChild(2), assignments)
    elif rule_name == 'LeftImpliesExprContext':
        return (not evaluate_tree(tree.getChild(2), assignments)) or evaluate_tree(tree.getChild(0), assignments)
    elif rule_name == 'NImpliesExprContext':
        return not ((not evaluate_tree(tree.getChild(0), assignments)) or evaluate_tree(tree.getChild(2), assignments))
    elif rule_name == 'LNImpliesExprContext':
        return not ((not evaluate_tree(tree.getChild(2), assignments)) or evaluate_tree(tree.getChild(0), assignments))
    raise ValueError(f"Unknown expression type: {rule_name}")

def generate_truth_table(expr):
    # Find variables
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