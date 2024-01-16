#===========#
#  PROGRAM  #
#===========#

def Program(body: list):
    return {
        "type": "Program",
        "body": body,
    }


def Identifier(name: str):
    return {
        "type": "Identifier",
        "name": name
    }

#============#
#  LITERALS  #
#============#

def StringLiteral(value):
    return {
        "type": "StringLiteral",
        "value": value,
        "raw": f"'{value}'"
    }


def NumericLiteral(value):
    return {
        "type": "NumericLiteral",
        "value": value,
        "raw": str(value)
    }


def BooleanLiteral(value):
    return {
        "type": "BooleanLiteral",
        "value": bool(value),
        "raw": "{value}"
    }


def NullLiteral():
    return {
        "type": "NullLiteral",
        "value": None,
        "raw": "null"
    }

#=============#
#  VARIABLES  #
#=============#

def VariableDeclaration(declarations: list):
    return {
        "type": "VariableDeclaration",
        "declarations": declarations
    }


def ConstantDeclaration(declarations: list):
    return {
        "type": "ConstantDeclaration",
        "declarations": declarations
    }


def VariableDeclarator(id: list, data_type: str | None, value: dict | None):
    return {
        "type": "VariableDeclarator",
        "id": id,
        "data_type": data_type,
        "value": value
    }


def ConstantDeclarator(id: list, data_type: str | None, value: dict):
    return {
        "type": "VariableDeclarator",
        "id": id,
        "data_type": data_type,
        "value": value
    }

#===============#
#  Expressions  #
#===============#

def BinaryExpression(left, operator: str, right):
    return {
        "type": "BinaryExpression",
        "left": left,
        "operator": operator,
        "right": right
    }


def ExpressionStatement(expression):
    return {
        "type": "ExpressionStatement",
        "expression": expression
    }


def AssignmentExpression(left, right):
    return {
        "type": "AssignmentExpression",
        "left": left,
        "right": right
    }


def MemberExpression(object, property):
    return {
        "type": "MemberExpression",
        "object": object,
        "property": property
    }

#=============#
#  FUNCTIONS  #
#=============#

def CallExpression(callee, arguments: list):
    return {
        "type": "CallExpression",
        "callee": callee,
        "arguments": arguments
    }
