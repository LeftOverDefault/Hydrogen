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
            return {"value": scope.get_variable(var_name=node["name"])}
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
            return {"value": answer}
        elif node_type == "AssignmentExpression":
            left = node["left"]
            right = self.interpret_node(node["right"], scope)["value"]
            if left["type"] == "Identifier":
                scope.assign_variable(left["name"], right)
            return {"left": left, "right": right}
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
            return scope.create_function(func_name=name, params=parameters, body=body)
        elif node_type == "ClassDeclaration":
            name = node["id"]["name"]
            body = []
            for sub_node in node["body"]:
                if sub_node != None:
                    body.append(sub_node)
            return scope.create_class(class_name=name, body=body)
        elif node_type == "ExpressionStatement":
            return self.interpret_node(node["expression"], scope)
        elif node_type == "MemberExpression":
            object_name = node["object"]["name"]
            member_name = node["property"]["callee"]["name"]
            arguments = []
            obj = scope.variables[object_name]
            for arg in node["property"]["arguments"]:
                arguments.append(arg["value"])
            for param, arg in zip(obj["value"]["parameters"], arguments):
                scope.declare_variable(var_name=param, value=arg)
            for node in obj["value"]["body"]:
                obj_body = self.interpret_node(node, scope)
            return obj_body
        elif node_type == "CallExpression":
            name = node["callee"]["name"]
            if name not in list(scope.variables.keys()):
                raise NameError(f"'{node["callee"]["name"]}' was not found globally.")
            else:
                id = scope.get_variable(name)
                if name not in scope.built_in_methods:
                    if id["type"] == "function":
                        temp_arguments = [self.interpret_node(arg, scope) for arg in node["arguments"]]
                        arguments = []
                        for arg in temp_arguments:
                            arguments.append(arg["value"])
                        function_env = scope.create_child_scope()

                        for param, arg in zip(id["parameters"], arguments):
                            function_env.declare_variable(var_name=param, value=arg)

                        result = None
                        for statement in id["body"]:
                            result = self.interpret_node(statement, function_env)
                        return result
                    elif id["type"] == "class":
                        class_env = scope.create_child_scope()
                        result = None
                        for statement in id["body"]:
                            result = self.interpret_node(statement, class_env)
                        return result
                else:
                    function_env = scope.create_child_scope()
                    args = []
                    for arg in node["arguments"]:
                        arg = self.interpret_node(arg, scope)
                        args.append(arg["value"])
                    return scope.variables[name](args)
        elif node_type == "EndOfFile":
            return None
        else:
            return node
