from src.utils.imports import *

from src.backend.lexer import Lexer
from src.frontend.parser import Parser
from src.runtime.environment import Environment
from src.runtime.interpreter import Interpreter


class Shell:
    def __init__(self) -> None:
        self.environment = Environment()

        self.running = True


    def run(self) -> None:
        os.system("cls")
        while self.running:
            lexer = Lexer()
            parser = Parser()
            interpreter = Interpreter(self.environment)

            prompt = input(">>> ")

            lexer.split_code(prompt)
            lexer.tokenize()
            parser.tokens = lexer.tokens


            ast_program = parser.create_program()
            program = interpreter.read_program(ast_program)
            
            if program != None:
                for node in program:
                    interpreter.interpret_node(node=node, scope=self.environment)
            else:
                pass