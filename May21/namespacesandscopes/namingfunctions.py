def sum(*items):
    """
    This function calculates sum of items
    """
    print('using our sum method')
    result = 0
    for item in items:
        result += item
    return result

result = sum(1,2,3,4,5)
print(result)
# This statement deletes the function from current namespace 
# so that built can be used
del sum
# We want to use built in method
result = sum([1,2,3,4,5,6])
print(result)

