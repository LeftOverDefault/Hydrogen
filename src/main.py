from src.utils.imports import *

from src.backend.lexer import Lexer
from src.frontend.parser import Parser
from src.runtime.environment import Environment
from src.runtime.interpreter import Interpreter


class Main:
    def __init__(self) -> None:
        self.tests = [test for test in os.walk("./tests")][0][2]
        self.lexer = Lexer()
        self.parser = Parser()
        self.environment = Environment()
        self.interpreter = Interpreter(self.environment)


    def run(self) -> None:
        for test in self.tests:
            # try:
                test_content = open(f"./tests/{test}", "r").read()

                self.lexer.split_code(test_content)
                self.lexer.tokenize()
                self.parser.tokens = self.lexer.tokens

                ast_program = self.parser.create_program()
                program = self.interpreter.read_program(ast_program)

                if program != None:
                    for node in program:
                        self.interpreter.interpret_node(node=node, scope=self.environment)
                    print(f"Test {test[:-3]} Passed")
                else:
                    print(f"Test {test[:-3]} Is Empty")
            # except Exception as e:
                # print(f"Test {test[:-3]} Failed With Exception:")
                # print(e)
