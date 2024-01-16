from src.utils.imports import *

from src.backend.token import *
from src.frontend.nodes import *


class Parser:
    def __init__(self) -> None:
        self.tokens = []


    def shift(self, shift_index: int = 1) -> dict:
        i = 0
        token = self.tokens[shift_index - 1]
        while i < shift_index:
            self.tokens.remove(self.tokens[0])
            i += 1
        return token


    def expect(self, expected_token, message):
        token = self.shift()
        if token["type"] != token_types[expected_token]:
            raise SyntaxError(message)
        else:
            return token


    def create_program(self) -> dict:
        body = []
        while len(self.tokens) > 0:
            if self.tokens[0]["type"] == token_types["eof"]:
                break
            else:
                body.append(self.create_nodes())
        return Program(body)


    def create_nodes(self) -> dict:
        if self.tokens[0]["type"] == token_types["number"]:
            return self.expression()
        elif self.tokens[0]["type"] == token_types["str"]:
            return self.expression()
        elif self.tokens[0]["type"] == token_types["bool"]:
            return self.expression()
        elif self.tokens[0]["type"] == token_types["("]:
            return self.expression()
        elif self.tokens[0]["type"] == keywords["null"]:
            self.shift()
            return NullLiteral()
        elif self.tokens[0]["type"] == token_types["ident"]:
            if self.tokens[1]["type"] == token_types["="]:
                identifier = Identifier(name=self.shift()["value"])
                self.shift()
                expression = self.expression()
                self.expect(";", "Expected Semicolon")
                return ExpressionStatement(expression=AssignmentExpression(left=identifier, right=expression))
            elif self.tokens[1]["type"] == token_types["."]:
                identifier = Identifier(name=self.shift()["value"])
                self.shift()
                property = self.create_nodes()
                return ExpressionStatement(expression=MemberExpression(object=identifier, property=property))
            elif self.tokens[1]["type"] == token_types["("]:
                identifier = Identifier(name=self.shift()["value"])
                arguments = []
                self.shift()
                while self.tokens[0]["type"] != token_types[")"]:
                    if self.tokens[0]["type"] == token_types[","]:
                        self.shift()
                    else:
                        arguments.append(self.create_nodes())
                self.expect(")", "Expected Closing Parenthesis after function call.")
                self.expect(";", "Expected Semicolon after function call.")
                return CallExpression(callee=identifier, arguments=arguments)
            else:
                return self.expression()
            # identifier = Identifier(self.shift()["value"])
            # elif self.tokens[0]["type"] == token_types["="]:
            #     self.shift()
            #     right = None
            #     while self.tokens[0]["type"] != token_types[";"]:
            #         right = self.create_nodes()
            #     self.expect(";", "Expected Semicolon after Variable Assignment.")
            #     return ExpressionStatement(expression=AssignmentExpression(left=identifier, right=right))
            # elif self.tokens[0]["type"] == token_types["+"]:
            #     self.shift()
            #     left = identifier
            #     right = None
            #     # while self.tokens[0]["type"] != token_types[";"]:
            #     right = self.create_nodes()
            #     # self.expect(";", "Expected Semicolon after Variable Assignment.")
            #     return BinaryExpression(left=left, operator="+", right=right)
            # else:
            #     return identifier
        elif self.tokens[0]["type"] == keywords["let"]:
            self.shift()
            id = Identifier(self.shift()["value"])
            data_type = None
            declarations = []
            if self.tokens[0]["type"] == token_types[":"]:
                self.shift()
                data_type = self.expect("ident", "Expected Identifier when declaring Variable Data Type")["value"]
            if self.tokens[0]["type"] == token_types[";"]:
                self.shift()
                value = None
            else:
                self.expect("=", "Expected Equivalence operator after Variable Declaration.")
                value = self.create_nodes()
                self.expect(";", "Expected Semicolon after Variable Declaration.")
                declarations.append(VariableDeclarator(id=id, data_type=data_type, value=value))
            return VariableDeclaration(declarations=declarations)
        elif self.tokens[0]["type"] == keywords["const"]:
            self.shift()
            id = Identifier(self.shift()["value"])
            data_type = None
            declarations = []
            if self.tokens[0]["type"] == token_types[":"]:
                self.shift()
                data_type = self.expect("ident", "Expected Identifier when declaring Variable Data Type")["value"]
            if self.tokens[0]["type"] == token_types[";"]:
                raise SyntaxError("Constant must be defined at initiation, not after.")
            else:
                self.expect("=", "Expected Equivalence operator after Variable Declaration.")
                value = self.create_nodes()
                self.expect(";", "Expected Semicolon after Variable Declaration.")
                declarations.append(VariableDeclarator(id=id, data_type=data_type, value=value))
            return ConstantDeclaration(declarations=declarations)
        elif self.tokens[0]["type"] == keywords["def"]:
            self.shift()
            id = Identifier(name=self.shift()["value"])
            parameters = []
            body = []
            if self.tokens[0]["type"] == token_types["("]:
                self.expect("(", "Expected Opening Parenthesis after Function Declaration.")
                while self.tokens[0]["type"] != token_types[")"]:
                    if self.tokens[0]["type"] == token_types[","]:
                        self.shift()
                    else:
                        parameters.append(Identifier(name=self.shift()["value"]))
                self.expect(")", "Expecting Closing Parenthesis after Function Declaration.")
            self.expect("{", "Expecting Opening Brace after Function Declaration.")
            while self.tokens[0]["type"] != token_types["}"]:
                body.append(self.create_nodes())
            self.expect("}", "Expecting Closing Brace after Function Declaration.")
            return FunctionDeclaration(id=id, parameters=parameters, body=body)
        elif self.tokens[0]["type"] == token_types["eof"]:
            return {"type": "END_OF_FILE"}
        else:
            raise SyntaxError(f"Unrecognized Token: {self.shift()["value"]}")


    def factor(self):
        if self.tokens[0]["value"].isdecimal():
            return NumericLiteral(value=int(self.shift()["value"]))
        elif self.tokens[0]["value"] == "(":
            self.shift()
            print(self.tokens[0])
            expression = self.expression()
            self.expect(")", "Expected Closing Parenthasis.")
            return expression
        elif self.tokens[0]["type"] == token_types["str"]:
            return StringLiteral(value=str(self.shift()["value"]))
        elif self.tokens[0]["type"] == token_types["bool"]:
            val = self.shift()["value"]
            if val == "true":
                value = True
            elif val == "false":
                value = False
            return BooleanLiteral(value=value)
        elif self.tokens[0]["type"] == token_types["ident"]:
            return Identifier(name=self.shift()["value"])
        else:
            value = self.shift()["value"]
            return NumericLiteral(value=float(value))


    def exponent(self):
        return self.binary_expression(function=self.factor, operators=(token_types["**"], token_types["%"], token_types["//"]))


    def term(self):
        return self.binary_expression(function=self.exponent, operators=(token_types["*"], token_types["/"]))


    def expression(self):
        return self.binary_expression(function=self.term, operators=(token_types["+"], token_types["-"]))


    def binary_expression(self, function, operators):
        left = function()
        while self.tokens[0]["type"] in operators:
            operator_token = self.shift()["value"]
            right = function()
            left = BinaryExpression(
                left=left, operator=operator_token, right=right)
        return left
