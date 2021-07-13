index = 1
result = 0
while index < 1000:
    if index % 3 ==0 or index % 5 == 0:
        result = result + index
    index = index + 1
print(result)