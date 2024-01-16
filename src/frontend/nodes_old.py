def Program(body: list):
    return {
        "type": "Program",
        "body": body,
        "sourceType": "script"
    }


def VariableDeclaration(declarations: list, kind: str):
    return {
        "type": "VariableDeclaration",
        "declarations": declarations,
        "kind": kind
    }


def VariableDeclarator(id: list, data_type: str | None, init: dict | None):
    return {
        "type": "VariableDeclarator",
        "id": id,
        "data_type": data_type,
        "init": init
    }


def BinaryExpression(left, operator: str, right):
    return {
        "type": "BinaryExpression",
        "left": left,
        "operator": operator,
        "right": right
    }


def ExpressionStatement(expression, directive):
    return {
        "type": "ExpressionStatement",
        "expression": expression,
        "directive": directive
    }


def CallExpression(callee, arguments):
    return {
        "type": "CallExpression",
        "callee": callee,
        "arguments": arguments
    }


def Identifier(name: str):
    return {
        "type": "Identifier",
        "name": name
    }


def NumericLiteral(value):
    return {
        "type": "NumericLiteral",
        "value": value,
        "raw": str(value)
    }

def StringLiteral(value):
    return {
        "type": "StringLiteral",
        "value": value,
        "raw": f"'{value}'"
    }

def BooleanLiteral(value):
    return {
        "type": "BooleanLiteral",
        "value": value,
        "raw": str(value)
    }

def FunctionDeclaration(id: dict, params: list, body: list, generator: bool, asynchronous: bool):
    return {
        "type": "FunctionDeclaration",
        "id": id,
        "params": params,
        "body": body,
        "generator": generator,
        "asynchronous": asynchronous
    }


def BlockStatement(body: list):
    return {
        "type": "BlockStatement",
        "body": body
    }


def ReturnStatement(argument):
    return {
        "type": "ReturnStatement",
        "argument": argument
    }


def MethodDefinition(key, computed, value, kind, static):
    return {
        "type": "MethodDefinition",
        "key": key,
        "computed": computed,
        "value": value,
        "kind": kind,
        "static": static
    }


def MemberExpression(computed: bool, object, property):
    return {
        "type": "MemberExpression",
        "computed": computed,
        "object": object,
        "property": property
    }


def SelfExpression():
    return {
        "type": "SelfExpression"
    }


def ClassDeclaration(id, super_class, body):
    return {
        "type": "ClassDeclaration",
        "id": id,
        "superClass": super_class,
        "body": body
    }


def ClassBody(body):
    return {
        "type": "ClassBody",
        "body": body
    }


def Comment(content):
    return {
        "type": "CommentLine",
        "content": content
    }


def IfStatement(condition, consequent, alternate):
    return {
        "type": "IfStatement",
        "condition": condition,
        "consequent": consequent,
        "alternate": alternate
    }


def SequenceExpression(expressions):
    return {
        "type": "SequenceExpression",
        "expressions": expressions
    }


def TupleExpression(elements):
    return {
        "type": "TupleExpression",
        "elements": elements
    }


def ArrayExpression(elements):
    return {
        "type": "ArrayExpression",
        "elements": elements
    }


def ObjectExpression(properties):
    return {
        "type": "ObjectExpression",
        "properties": properties
    }


def Property(key, value):
    return {
        "type": "Property",
        "key": key,
        "value": value
    }


def AssignmentExpression(left, right):
    return {
        "type": "AssignmentExpression",
        "left": left,
        "right": right
    }


def ImportDeclaration(specifiers, source):
    return {
        "type": "ImportDeclaration",
        "specifiers": specifiers,
        "source": source
    }


def ImportDefaultSpecifier(local):
    return {
        "type": "ImportDefaultSpecifier",
        "local": local
    }


def WhileStatement(condition, body):
    return {
        "type": "WhileStatement",
        "condition": condition,
        "body": body
    }