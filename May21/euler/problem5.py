max_number = 4
maximum_multiple = 1
for index in range(1, max_number+1):
    maximum_multiple *= index

for index in range(max_number, maximum_multiple+1,max_number):
    for number in range(2,max_number+1):
        if index%number != 0:
            break
    else:
        print(f"{index} is divisible by all the numbers from 1 to {max_number}")
        break