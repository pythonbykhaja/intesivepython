# This program will print all the numbers from 1 to 100 
# apart from multiples of 7

index = 1
max_number = 100
while index <= max_number:
    if index % 7 == 0:
        index = index+1
        continue
    print(index)
    index = index + 1
