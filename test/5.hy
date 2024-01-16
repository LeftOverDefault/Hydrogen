def function(parameter) {
    print(parameter);
    return "Exit Code 0";
}

let func = function("Hello World!");

print(func);

def async asynchronous_function(parameter) {
    await print(parameter);
}

def * generator_function(parameter) {
    yield;
}