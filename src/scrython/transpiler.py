import sys
import ast

class Transpiler(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current_class = None
        self.current_function = None
    
    def visit_ImportFrom(self, node):
        if not 'scrython' in node.module:
            raise Exception("Importing modules other than scrython is currently unsupported.")
        if node.module is not 'scrython.types':
            raise Exception("What are you even importing lmao")
        self.generic_visit(node)
    
    def visit_Import(self, node):
        if not 'scrython' in node.module:
            raise Exception("Importing modules other than scrython is currently unsupported.")
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        self.current_class = node
        self.generic_visit(node)
        self.current_class = None
    
    def visit_IfExp(self, node):
        if self.current_class is None:
            raise Exception("No expressions can be ran outside of a class")
        self.generic_visit(node)
    
    def visit_Expression(self, node):
        if self.current_class is None:
            raise Exception("No expressions can be ran outside of a class")
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        if self.current_class is None:
            raise Exception("You cannot define a function outside of a class")

        for decorator in node.decorator_list:
            print(type(decorator))

        self.current_function = node
        self.generic_visit(node)
        self.current_function = None