# This program is solution to project euler problem 2
# https://projecteuler.net/problem=2

first_number = 1
second_number = 2
sum_of_even_numbers = 2
max_number = 4000000
while True:
    third_number = first_number + second_number
    if third_number >= max_number:
        break
    if third_number%2 == 0:
        sum_of_even_numbers += third_number
    first_number = second_number
    second_number = third_number

print(f'Sum of even valued numbers in fibonnci series is {sum_of_even_numbers}')