#def sum(number1, number2):
#    pass

def sum(*args):
    print(type(args))
    result = 0
    for arg in args:
        result += arg
    return result


result = sum(1,2)
print(result)
result = sum(1,2,3,4,5,6,7,8,9)
print(result)
result = sum()
print(result)

def explain_kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} = {value}")


explain_kwargs(name='IHub', course='Python', duration='3')

def fun_function(*args, **kwargs):
    print(f"args are {args}")
    print(f"keyword args are {kwargs}")


fun_function('python.direct', 'learningthoughts.academy', blog='python.direct')


def rule_function(number, debug=True, *args, **kwargs):
    pass


