def is_even(number):
    return number % 2 == 0


try:
    is_even('Hello')
except Exception as e:
    print("Enter the arguments correctly")
finally:
    print('Executed the program successfully')
