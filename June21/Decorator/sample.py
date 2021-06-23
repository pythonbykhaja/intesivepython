def capitalize(function):
    def inner_function():
        result = function()
        return result.capitalize()
    return inner_function

def detail(function):
    def wrapper(*args, **kwargs):
        print(f"Running function {function.__name__}")
        print(f"Positional Arguments are {args}")
        print(f"Keyword argumetns are {kwargs}")
        result = function(*args, **kwargs)
        print(f"Result is {result}")
        return result
    return wrapper

@detail        
@capitalize
def say_hello():
    return "hello!"

@detail
def add(x,y):
    return x+y

print(say_hello())

print(add(3,5))

print(add(x=100, y=100))