from src.utils.imports import *


class Stack:
    def __init__(self, max_size: int, stack: list = []) -> None:
        self.max_size = max_size
        self.top = -1
        self.stack = stack


    def __str__(self):
        return self.stack


    def is_full(self) -> bool:
        if self.top == self.max_size - 1:
            return True
        else:
            return False


    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        else:
            return False


    def push(self, data) -> int:
        if self.is_full() == True:
            raise SyntaxError(f"Stack is full - {data} was not added.")
        else:
            self.top += 1
            self.stack[self.top] = data
        return self.top


    def pop(self):
        if self.is_empty() == True:
            raise SyntaxError(f"Stack is empty - Nothing to pop.")
            popped_item = None
        else:
            popped_item = self.stack[self.top]
            self.top -= 1
        return popped_item, self.top


    def peek(self):
        if self.is_empty() == True:
            raise SyntaxError(f"Stack is empty - Nothing to pop.")
            peeked_item = None
        else:
            peeked_item = self.stack[self.top]
        return peeked_item
