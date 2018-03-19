from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CfgParser import CfgParser
    from .CfgLexer import CfgLexer
    from .CfgVisitor import CfgVisitor
else:
    from CfgParser import CfgParser
    from CfgLexer import CfgLexer
    from CfgVisitor import CfgVisitor


class CfgCompiler:
    def __init__(self, filepath):
        self.input = FileStream(filepath)
        self.lexer = CfgLexer(self.input)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = CfgParser(self.stream)
        self.tree = self.parser.prog()

    def compile(self):
        return CfgVisitor(self.stream).visit(self.tree)

    def draw_parse_tree(self):
        # TODO: ADD graphviz support
        # Now Prints in LISP Style
        # (root child1 child2 ... childN)
        print(self.tree.toStringTree(recog=self.parser))
