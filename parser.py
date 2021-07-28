#!/usr/bin/env python3

import tatsu
from tatsu.ast import AST

GRAMMAR_PATH = 'fuego.ebnf'

def load_model(path):
    '''Import and compile the Fuego grammar from an external file.'''

    with open(path) as f:
        return tatsu.compile(f.read())

# import the fuego grammar as a global variable
model = load_model(GRAMMAR_PATH)

class FuegoSemantics:
    def number(self, ast):
        return int(ast)

    def term(self, ast):
        if not isinstance(ast, AST):
            return ast
        elif ast.op == '*':
            return ast.left * ast.right
        elif ast.op == '/':
            return ast.left / ast.right
        else:
            raise Exception('Unknown operator', ast.op)

    def expression(self, ast):
        if not isinstance(ast, AST):
            return ast
        elif ast.op == '+':
            return ast.left + ast.right
        elif ast.op == '-':
            return ast.left - ast.right
        else:
            raise Exception('Unknown operator', ast.op)

def repl():
    '''A repl for debugging the parser.'''

    import sys
    import pprint

    def readline(prompt='> '):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        return sys.stdin.readline()

    while line := readline():
        try:
            # parse the AST
            ast = model.parse(line)

            # print the raw AST
            print('AST:')
            pprint.pprint(ast, indent=2, width=20)

            # evaluate the AST
            result = model.parse(line, semantics=FuegoSemantics())

            # print the result
            print('EVAL:')
            pprint.pprint(result, indent=2, width=20)

        except Exception as e:
            print(type(e), e)

if __name__ == '__main__':
    repl()
