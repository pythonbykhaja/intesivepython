number = 190
index = 2

while index < number:
    if number%index == 0:
        print("Not a prime")
        break
    index += 1
else:
    print("Prime number")
