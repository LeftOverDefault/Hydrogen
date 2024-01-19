from src.utils.imports import *

from src.runtime.func.functions import *


class Environment:
    def __init__(self, parent=None) -> None:
        self.variables = {}
        self.constants = []
        self.built_in_methods = ["print", "abs", "vec2", "vec3", "max", "min", "sqrt", "quit"]
        self.parent = parent
        self.define_builtin_methods()

    def define_builtin_methods(self):
        self.declare_variable(var_name="print", value=lambda args: print_line(args))
        self.declare_variable(var_name="max", value=lambda args: max(args))
        self.declare_variable(var_name="min", value=lambda args: min(args))
        self.declare_variable(var_name="abs", value=lambda args: absolute(args))
        self.declare_variable(var_name="vec2", value=lambda args: vector_2(args))
        self.declare_variable(var_name="vec3", value=lambda args: vector_3(args))
        self.declare_variable(var_name="quit", value=lambda args: quit_func(args))
        self.declare_variable(var_name="sqrt", value=lambda args: sqrt(args))
        self.declare_variable(var_name="pi", value=3.141592653589793)
        self.declare_variable(var_name="e", value=2.718281828459045)

    def declare_variable(self, var_name, value):
        self.variables[var_name] = value

    def create_function(self, func_name, params, body):
        self.declare_variable(func_name, {"parameters": params, "body": body})

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
