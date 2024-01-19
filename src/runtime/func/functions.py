from src.utils.imports import *


def print_line(args):
    string = ""
    for arg in args:
        string += str(arg) + " "
    print(string)


def absolute(args):
    if len(args) > 1:
        raise ValueError("Absolute function takes 1 argument.")
    else:
        arg = args[0]
        try:
            _arg = int(arg)
        except:
            raise TypeError("Absolute function takes only Numerics.")
        if arg < 0:
            return -arg
        else:
            return arg


def vector_2(args):
    if len(args) != 2:
        raise ValueError("Vector 2 takes 2 arguments.")
    else:
        x = args[0]
        y = args[1]
        try:
            _x = float(x)
            _y = float(y)
        except:
            raise TypeError("Vector 2 takes only Numerics.")
        return (x, y)


def vector_3(args):
    if len(args) != 3:
        raise ValueError("Vector 3 takes 3 arguments.")
    else:
        x = args[0]
        y = args[1]
        z = args[2]
        try:
            _x = float(x)
            _y = float(y)
            _z = float(z)
        except:
            raise TypeError("Vector 3 takes only Numerics.")
        return (x, y, z)


def sqrt(args):
    if len(args) != 1:
        raise TypeError("Square Root takes 1 argument.")
    else:
        arg = args[0]
        try:
            _arg = float(arg)
        except:
            raise TypeError("Vector 3 takes only Numerics.")
        if arg < 0:
            raise ValueError("Cannot Square Root negative numbers.")
        return math.sqrt(arg)


def quit_func(args):
    string = ""
    for arg in args:
        string += str(arg) + " "
    quit(string)