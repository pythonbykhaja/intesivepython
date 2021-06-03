min = 100
max = 1000
for number in range(min,max+1):
    # if number is prime
    for index in range(2,number//2):
        if number%index == 0:
            break
    else:
        print(number)