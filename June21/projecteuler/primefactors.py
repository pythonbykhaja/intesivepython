from numerical.operations import factors, factorial
from numerical.query import is_prime
# numerical => sub directory containing python files => package
# operations => python module

print(factorial(5))

# problem is to find sum of prime factors
factors_list = factors(13195)
sum = 0
for value in factors_list:
    if is_prime(value):
        sum += value







