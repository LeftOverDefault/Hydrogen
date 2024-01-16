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
            type = str(node["type"])
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
            # function_env = scope.create_child_scope()
            # func_name = node["id"]["name"]
            # func_parameters = []
            # for parameter in node["parameters"]:
            #     func_parameters.append(parameter["name"])
            #     function_env.declare_variable(var_name=parameter["name"], value="")
            # body = []
            # for sub_node in node["body"]:
            #     sub_node = self.interpret_node(sub_node, function_env)
            #     if sub_node != None:
            #         body.append(sub_node)
            # scope.create_function(func_name=func_name, params=func_parameters, body=body)
            name = node["id"]["name"]
            parameters = []
            body = []
            for parameter in node["parameters"]:
                parameters.append(parameter["name"])
            for sub_node in node["body"]:
                if sub_node != None:
                    body.append(sub_node)
            scope.create_function(func_name=name, params=parameters, body=body)
        elif type == "ExpressionStatement":
            return self.interpret_node(node, scope)
        # elif type == "MemberExpression":
            # expression = self.interpret_node(node["expression"], scope)
            # object = expression["object"]["name"]
            # property = expression["property"]["name"]
        elif type == "AssignmentExpression":
            left = node["left"]
            right = self.interpret_node(node["right"], scope)
            return {"left": left, "right": right}
        elif type == "CallExpression":
            name = node["callee"]["name"]
            if name not in list(scope.variables.keys()):
                raise NameError(f"'{node["callee"]["name"]}' was not found globally.")
            else:
                function = scope.get_variable(name)["value"]
                # print(function["body"][0])
                # print(function["body"][1])
                if name not in scope.built_in_methods:
                    temp_arguments = [self.interpret_node(arg, scope) for arg in node["arguments"]]
                    arguments = []
                    for arg in temp_arguments:
                        arguments.append(arg["value"])
                        
                    # for node in function["body"]:
                        # temp_arguments = node["arguments"]
                        # for arg in temp_arguments:
                            # if arg["type"] == "Identifier":
                                # arguments.append(arg["name"])

                    function_env = scope.create_child_scope()

                    for param, arg in zip(function["parameters"], arguments):
                        function_env.declare_variable(var_name=param, value=arg)
                    
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
                    scope.variables[name](args)
                    return None


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
