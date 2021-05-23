# Hacker rank if else problem 
# url of the problem https://www.hackerrank.com/challenges/py-if-else/
n = int(input(''))
remainder = n % 2
if 1<= n <= 100 and remainder != 0:
    print('Weird') # odd number
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
elif  20 < n <=100 :
    print('Not Weird')
else:
    print('Not in Range')
    