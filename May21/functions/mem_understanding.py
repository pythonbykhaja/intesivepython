def increment(number):
    print(f"memory location of number is {id(number)}")
    number += 1
    print(f"memory location of number is {id(number)}")
    return number

def add_number(numbers, number):
    import copy
    copy_numbers = copy.deepcopy(numbers)
    print(f"id of numbers is {id(copy_numbers)}")
    copy_numbers.append(number)
    print(f"Copy numbers are {copy_numbers}")
    print(f"id of numbers is {id(copy_numbers)}")


numbers = [1,2,3]
print(f"id of numbers is {id(numbers)}")
add_number(numbers, 100)
print(f"id of numbers is {id(numbers)}")
print(numbers)
