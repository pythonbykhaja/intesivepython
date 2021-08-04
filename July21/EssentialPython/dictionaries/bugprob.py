index = 2
number = 190
while index < number:
    if number%index == 0:
        print('prime')
        break
    index += 1
else:
    print('not prime')