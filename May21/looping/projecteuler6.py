# This program tries to solve the project euler 6
index = 1
sum_of_numbers = 0
sum_of_squares = 0
while index <= 100:
    # Calculate the sum of the numbers by adding all numbers
    sum_of_numbers = sum_of_numbers + index
    # Caclulating the square og the number and adding it to the index
    sum_of_squares = sum_of_squares + (index ** 2)


result = (sum_of_numbers ** 2) - sum_of_squares
print(result)
