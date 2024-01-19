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
            node_type = str(node["type"])
        else:
            node_type = None
        if node_type == "StringLiteral":
            return {"value": node["value"], "type": node_type}
        elif node_type == "NumericLiteral":
            return {"value": node["value"], "type": node_type}
        elif node_type == "BooleanLiteral":
            return {"value": node["value"], "type": node_type}
        elif node_type == "Identifier":
            return scope.get_variable(var_name=node["name"])
        elif node_type == "BinaryExpression":
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
        elif node_type == "VariableDeclaration":
            for declaration in node["declarations"]:
                declaration = self.interpret_node(declaration, scope)
                id = declaration["id"]["name"]
                value = declaration["value"]
                data_type = declaration["data_type"]
                is_declared_data_type = True

                if value["type"] == "CallExpression":
                    value = self.interpret_node(value, scope)
                else:
                    value = self.interpret_node(value, scope)["value"]
                if data_type == "int":
                    if type(value) == int:
                        is_declared_data_type = True
                    else:
                        is_declared_data_type = False
                elif data_type == "str":
                    if type(value) == str:
                        is_declared_data_type = True
                    else:
                        is_declared_data_type = False
                elif data_type == "float":
                    if type(value) == float:
                        is_declared_data_type = True
                    else:
                        is_declared_data_type = False
                elif data_type == "bool":
                    if type(value) == bool:
                        is_declared_data_type = True
                    else:
                        is_declared_data_type = False

                if is_declared_data_type == False:
                    raise TypeError(f"Data Type `{type(value).__name__}` cannot be resolved for Variable `{id}` with declared Data Type of `{data_type}`.")

                scope.variables[id] = value
        elif node_type == "ConstantDeclaration":
            for declaration in node["declarations"]:
                declaration = self.interpret_node(declaration, scope)
                id = declaration["id"]["name"]
                value = self.interpret_node(declaration["value"], scope)["value"]
                scope.variables[id] = value
                scope.constants.append(id)
        elif node_type == "VariableDeclarator":
            return {"id": node["id"], "value": node["value"], "data_type": node["data_type"]}
        elif node_type == "ConstantDeclarator":
            return {"id": node["id"], "value": node["value"], "data_type": node["data_type"]}
        elif node_type == "FunctionDeclaration":
            name = node["id"]["name"]
            parameters = []
            body = []
            for parameter in node["parameters"]:
                parameters.append(parameter["name"])
            for sub_node in node["body"]:
                if sub_node != None:
                    body.append(sub_node)
            scope.create_function(func_name=name, params=parameters, body=body)
        elif node_type == "ExpressionStatement":
            return self.interpret_node(node["expression"], scope)
        # elif type == "MemberExpression":
            # expression = self.interpret_node(node["expression"], scope)
            # object = expression["object"]["name"]
            # property = expression["property"]["name"]
        elif node_type == "AssignmentExpression":
            left = node["left"]
            right = self.interpret_node(node["right"], scope)["value"]
            if left["type"] == "Identifier":
                scope.assign_variable(left["name"], right)
            return {"left": left, "right": right}
        elif node_type == "CallExpression":
            name = node["callee"]["name"]
            if name not in list(scope.variables.keys()):
                raise NameError(f"'{node["callee"]["name"]}' was not found globally.")
            else:
                function = scope.get_variable(name)["value"]
                if name not in scope.built_in_methods:
                    temp_arguments = [self.interpret_node(arg, scope) for arg in node["arguments"]]
                    arguments = []
                    for arg in temp_arguments:
                        arguments.append(arg["value"])
                    function_env = scope.create_child_scope()

                    for param, arg in zip(function["parameters"], arguments):
                        function_env.declare_variable(
                            var_name=param, value=arg)

                    result = None
                    for statement in function["body"]:
                        result = self.interpret_node(statement, function_env)
                    # return self.interpret_node(function["body"])
                    return result
                else:
                    args = []
                    for arg in node["arguments"]:
                        arg = self.interpret_node(arg, scope)["value"]
                        args.append(arg)
                    return scope.variables[name](args)

                # if name not in scope.built_in_methods:
                #     body = scope.variables[name]["body"]
                #     params = scope.variables[name]["parameters"]
                #     for parameter, arg in zip(params, args):
                #         scope.declare_variable(var_name=parameter, value=arg)
                #     for node_num in range(len(body)):
                #         body[node_num](args)
                # if name in scope.built_in_methods:
                    # else:
                # return self.interpret_node(scope.variables[name]["body"], scope)
        else:
            return node
