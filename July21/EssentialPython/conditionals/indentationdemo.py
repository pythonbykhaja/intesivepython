
for index in range(10, 1000):
    for prime_index in range(2,index):
        if index%prime_index == 0:
            print(f"{index} is not prime")
            break
    else:
        print(f"{index} is prime")

