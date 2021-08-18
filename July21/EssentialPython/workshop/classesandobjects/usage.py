from basics import Student
from numbers import Number, AdvancedNumber

if __name__ == '__main__':
    number = Number(19)
    if number.is_prime():
        print(f"{number.number} is prime")

    number2 = AdvancedNumber(23)
    if number2.is_prime():
        print(f"{number2.number} is prime")