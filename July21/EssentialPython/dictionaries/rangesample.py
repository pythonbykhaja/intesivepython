number = 19
for index in range(2,19):
    if number%index == 0:
        print('not prime')
        break
else:
    print('prime')