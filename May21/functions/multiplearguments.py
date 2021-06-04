def sum(*args):
    '''
    This function will calculate sum of arguments
    '''
    sum = 0
    for arg in args:
        sum += arg
    print(sum)
    return sum

sum(1)
sum(1,2,3,4,5,6,7,8)

def print_args(*args):
    print(f"Type is {type(args)} and Value is {args}")
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    print(f"Type is {type(kwargs)}")
    print(kwargs)
    for argument,value in kwargs:
        print(f"{argument}  ==> {value}")

print_args(1,2,3)
print_kwargs(name='Python', usage= 'Every where')

def print_data(data, start=10, end=100):
    pass

def print_data_again(data,*args,**kwargs):
    pass

print_data_again([1,2,3],start=0, end=1)

print_data(range(1,1000))

print_data_again([1,2,3],1,3)



