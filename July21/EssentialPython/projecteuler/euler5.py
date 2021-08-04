max_number = 5

hcm = 1
index = 1
while index <= max_number:
    hcm *= index
    index += 1

lcm = max_number
while lcm <= hcm:
    index = 1
    while index <= max_number:
        if lcm % index != 0:
            break
        index = index + 1
        
    else:
        print(lcm)
        break
    lcm = lcm + max_number