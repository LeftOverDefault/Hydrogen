# At this point I've just about McFuckin had it...


from src.utils.imports import *
from src.runtime.environment import Environment


class Interpreter:
    def __init__(self, scope: Environment) -> None:
        self.scope = scope

    def read_program(self, program):
        self.program = program
        body = self.program["body"]
        if len(body) > 0:
            return body
        else:
            return None


    def interpret_node(self, node, scope: Environment):
        if node != None:
            type = node["type"]
        else:
            type = None
        if type == "StringLiteral":
            return {"value": node["value"], "type": type}
        elif type == "NumericLiteral":
            return {"value": node["value"], "type": type}
        elif type == "BooleanLiteral":
            return {"value": node["value"], "type": type}
        elif type == "Identifier":
            return scope.get_variable(var_name=node["name"])
        elif type == "BinaryExpression":
            left = self.interpret_node(node["left"], scope)["value"]
            operator = node["operator"]
            right = self.interpret_node(node["right"], scope)["value"]
            if operator == "+":
                answer = left + right
            if operator == "-":
                answer = left - right
            if operator == "*":
                answer = left * right
            if operator == "/":
                answer = left / right
            if operator == "%":
                answer = left % right
            if operator == "**":
                answer = left ** right
            if operator == "//":
                answer = left // right
            return {"type": "NumericLiteral", "value": answer}
        elif type == "CallExpression":
            if node["callee"]["name"] not in list(scope.variables.keys()):
                raise NameError(f"{node["callee"]["name"]} not found globally.")
            else:
                args = []
                for arg in node["arguments"]:
                    arg = self.interpret_node(arg, scope)["value"]
                    args.append(arg)
                scope.variables[node["callee"]["name"]](args)
        elif type == "VariableDeclaration":
            for declaration in node["declarations"]:
                declaration = self.interpret_node(declaration, scope)
                id = declaration["id"]["name"]
                value = self.interpret_node(declaration["value"], scope)["value"]
                scope.variables[id] = value
        elif type == "ConstantDeclaration":
            for declaration in node["declarations"]:
                declaration = self.interpret_node(declaration, scope)
                id = declaration["id"]["name"]
                value = self.interpret_node(declaration["value"], scope)["value"]
                scope.variables[id] = value
                scope.constants.append(id)
        elif type == "VariableDeclarator":
            return {"id": node["id"], "value": node["value"]}
        elif type == "ConstantDeclarator":
            return {"id": node["id"], "value": node["value"]}
        elif type == "FunctionDeclaration":
            function_env = scope.create_child_scope()
            func_name = node["id"]
            func_params = []
            for param in node["params"]:
                func_params.append(param["name"])
            body = self.interpret_node(node["body"], function_env)
            scope.create_function(func_name=func_name, params=func_params, body=body)
        elif type == "ExpressionStatement":
            if node["expression"]["type"] == "CallExpression":
                expression = self.interpret_node(node["expression"], scope)
                left = expression["left"]["name"]
                right = expression["right"]["value"]
                scope.assign_variable(left, right)
            # elif node["expression"]["type"] == "MemberExpression":
                # expression = self.interpret_node(node["expression"], scope)
                # object = expression["object"]["name"]
                # property = expression["property"]["name"]
        elif type == "AssignmentExpression":
            left = node["left"]
            right = self.interpret_node(node["right"], scope)
            return {"left": left, "right": right}
        else:
            return node
