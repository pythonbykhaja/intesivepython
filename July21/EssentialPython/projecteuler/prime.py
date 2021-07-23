number = 19
index = 2

while index < number:
    if number%index == 0:
        is_prime = False
        break
    index += 1

if is_prime:
    print("Prime Number")
else:
    print("Not a prime number")