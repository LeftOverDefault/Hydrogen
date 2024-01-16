from src.utils.imports import *

from src.runtime.func.functions import *


class Environment:
    def __init__(self, parent=None) -> None:
        self.variables = {}
        self.constants = []
        self.parent = parent
        self.define_builtin_methods()


    def define_builtin_methods(self):
        self.declare_variable("print", lambda args: print_line(args))


    def declare_variable(self, var_name, value):
        self.variables[var_name] = value


    def get_variable(self, var_name):
        if var_name in list(self.variables.keys()):
            if self.variables[var_name] == None:
                return {"value": "null"}
            else:
                return {"value": self.variables[var_name]}
        if self.parent != None:
            if var_name in list(self.parent.variables.keys()):
                return self.parent.variables[var_name]
            else:
                raise NameError(f"Variable '{var_name}' is not defined.")


    def assign_variable(self, var_name, value):
        if var_name in self.constants:
            raise SyntaxError(f"Cannot update the value of '{var_name}' as it was declared as Constant.")
        elif var_name not in list(self.variables.keys()):
            raise NameError(f"Variable '{var_name}' is not defined.")
        else:
            self.variables[var_name] = value


    def contains(self, var_name):
        return var_name in self.variables.keys()


    def create_child_scope(self):
        return Environment(parent=self)
