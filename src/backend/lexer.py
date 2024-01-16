from src.utils.imports import *
from src.backend.token import token_types, keywords, token


def is_skippable(char):
    return char in [" ", "\n", "\t", "\r", "\a", "\f", "\v", "\b"]

def is_alpha(char):
    return char.lower() != char.upper()

def is_numeric(char):
    return char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Lexer:
    def __init__(self) -> None:
        self.characters = []
        self.tokens = []


    def split_code(self, code) -> None:
        for char in code:
            self.characters.append(char)


    def shift(self, shift_index: int = 1) -> str:
        i = 0
        char = self.characters[shift_index - 1]
        while i < shift_index:
            self.characters.remove(self.characters[0])
            i += 1
        return str(char)


    def tokenize(self) -> None:
        while (len(self.characters) != 0):
            if (self.characters[0] == "\""):
                string = ""
                self.shift()
                while (len(self.characters) > 0 and self.characters[0] != "\""):
                    string += str(self.shift())
                self.shift()
                self.tokens.append(token(value=string, token_type=token_types["str"]))
            elif (self.characters[0] == "'"):
                string = ""
                self.shift()
                while (len(self.characters) > 0 and self.characters[0] != "'"):
                    string += str(self.shift())
                self.shift()
                self.tokens.append(token(value=string, token_type=token_types["str"]))
            elif (self.characters[0] == "+"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["+"]))
            elif (self.characters[0] == "-"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["-"]))
            elif (self.characters[0] == "*"):
                if self.characters[1] == "*":
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types["**"]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types["*"]))
            elif (self.characters[0] == "/"):
                if self.characters[1] == "/":
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types["//"]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types["/"]))
            elif (self.characters[0] == "%"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["%"]))
            elif (self.characters[0] == ";"):
                self.tokens.append(token(value=self.shift(), token_type=token_types[";"]))
            elif (self.characters[0] == ":"):
                self.tokens.append(token(value=self.shift(), token_type=token_types[":"]))
            elif (self.characters[0] == "="):
                if (self.characters[1] == "="):
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types["=="]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types["="]))
            elif (self.characters[0] == "!"):
                if (self.characters[1] == "="):
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types["!="]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types["!"]))
            elif (self.characters[0] == ">"):
                if (self.characters[1] == "="):
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types[">="]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types[">"]))
            elif (self.characters[0] == "<"):
                if (self.characters[1] == "="):
                    self.tokens.append(token(value=self.shift() + self.shift(), token_type=token_types["<="]))
                else:
                    self.tokens.append(token(value=self.shift(), token_type=token_types["<"]))
            elif (self.characters[0] == "("):
                self.tokens.append(token(value=self.shift(), token_type=token_types["("]))
            elif (self.characters[0] == ")"):
                self.tokens.append(token(value=self.shift(), token_type=token_types[")"]))
            elif (self.characters[0] == "["):
                self.tokens.append(token(value=self.shift(), token_type=token_types["["]))
            elif (self.characters[0] == "]"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["]"]))
            elif (self.characters[0] == "{"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["{"]))
            elif (self.characters[0] == "}"):
                self.tokens.append(token(value=self.shift(), token_type=token_types["}"]))
            elif (self.characters[0] == "."):
                self.tokens.append(token(value=self.shift(), token_type=token_types["."]))
            elif (self.characters[0] == ","):
                self.tokens.append(token(value=self.shift(), token_type=token_types[","]))
            else:
                if (is_skippable(self.characters[0])):
                    self.shift()
                elif (is_alpha(self.characters[0])):
                    identifier = ""
                    while (len(self.characters) > 0) and (is_alpha(self.characters[0]) or self.characters[0] == "_" or is_numeric(self.characters[0])):
                        identifier += self.shift()
                    if (identifier in keywords):
                        self.tokens.append(token(identifier, keywords[identifier]))
                    elif (identifier.lower() in keywords):
                        raise NameError
                    else:
                        self.tokens.append(token(identifier, token_types["ident"]))
                elif (is_numeric(self.characters[0])):
                    number = ""
                    has_dot = False
                    while (len(self.characters) > 0 and (is_numeric(self.characters[0]) or (self.characters[0] == "." and has_dot == False))):
                        if self.characters[0] == "." and has_dot == False:
                            has_dot = True
                        number += self.shift()
                    self.tokens.append(token(value=number, token_type=token_types["number"]))
                else:
                    # Throw Unknown Character Error
                    # return None
                    raise SyntaxError(f"Unrecognized Character: {self.characters[0]}")

        self.tokens.append(token(value="eof", token_type=token_types["eof"]))