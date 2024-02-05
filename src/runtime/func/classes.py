# from src.utils.imports import *


class List:
    def __init__(self, max_size: int, list: list = []) -> None:
        self.max_size = max_size
        self.list = list


    def __str__(self):
        return str(self.list)


    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False


    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False


    def append_item(self, item):
        if self.is_full() == True:
            raise SyntaxError(f"List is full - '{item}' not Appended.")
        else:
            self.list.append(item)


    def remove_item(self, item):
        if self.is_empty() == True:
            raise SyntaxError(f"List is empty - '{item}' not Removed.")
        elif item not in self.list:
            raise SyntaxError(f"List does not contain Item - '{item}' not in List.")
        else:
            self.list.remove(item)


    def search(self, item):
        if self.is_empty() == True:
            raise SyntaxError(f"List is empty - '{item}' not in List.")
        else:
            return item in self.list


    def insert(self, pos, item):
        if self.is_empty() == True:
            raise SyntaxError(f"List is empty - '{item}' not Inserted.")
        if self.is_full() == True:
            raise SyntaxError(f"List is full - '{item}' not Inserted.")
        else:
            self.list.insert(pos, item)


    def length(self):
        return len(self.list)


    def index(self, item):
        if self.is_empty() == True:
            raise SyntaxError(f"List is empty - '{item}' has no Index.")
        elif item not in self.list:
            raise SyntaxError(f"List does not contain Item - '{item}' not in List.")
        else:
            return self.list.index(item)


    def pop(self, pos=None):
        if self.is_empty() == True:
            raise SyntaxError(f"List is empty - No Item at index {pos}.")
        if pos != None and pos > len(self.list) - 1:
            raise SyntaxError(f"Invalid Index - Index '{pos}' out of range.")
        elif pos == None:
            item = self.list.pop()
            return item
        else:
            item = self.list.pop(pos)
            return item


class Stack:
    def __init__(self, max_size: int, stack: list = []) -> None:
        self.max_size = max_size
        self.top = -1
        self.stack = stack


    def __str__(self):
        return str(self.stack)


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
            raise SyntaxError(f"Stack is full - '{data}' not Pushed.")
        else:
            self.top += 1
            self.stack.append(data)
            # self.stack[self.top] = data
        return self.top


    def pop(self):
        if self.is_empty() == True:
            raise SyntaxError(f"Stack is empty - Nothing to Pop.")
            popped_item = None
        else:
            popped_item = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
        return popped_item


    def peek(self):
        if self.is_empty() == True:
            raise SyntaxError(f"Stack is empty - Nothing to Peek.")
        else:
            return self.stack[self.top]
    

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self, max_size: int, queue: list = []) -> None:
        self.max_size = max_size
        self.queue = queue

    
    def __str__(self):
        return str(self.queue)


    def is_full(self):
        if len(self.queue) == self.max_size:
            return True
        else:
            return False


    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    

    def en_queue(self, item):
        if self.is_full() == True:
            raise SyntaxError(f"Queue is full - {item} not En-Queued.")
        else:
            self.queue.append(item)


    def de_queue(self):
        if self.is_empty() == True:
            raise SyntaxError("Queue is empty - Nothing to De-Queue.")
        else:
            return self.queue.pop(0)
        
    
    def peek(self):
        if self.is_empty() == True:
            raise SyntaxError(f"Queue is empty - Nothing to Peek.")
            peeked_item = None
        else:
            peeked_item = self.queue[0]
        return peeked_item


if __name__ == "__main__":
    pass