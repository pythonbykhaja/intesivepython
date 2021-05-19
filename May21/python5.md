### How the programs are executed
* Interpreter/Compiler will read the program and execute it statement by statement
* Lets look at the following section
```
1. Take input
2. check if the input is even
3. print input is even
4. print input is odd
```
* If we consider the above statements
  * for even number 1,2,3 lines/statement should be executed
  * for odd number 1,2,4 should be executed
* To solve this in programming languages we have conditional statements which help in selecting the lines/statements valid for the input provided
```
1. Take input
2. if input is even
3. then print input is even
4. else print input is odd
```
* Lets look of following section
```
1. Take input from user (date)
2. if date is b/w march and june 
3. print summer
4. else if date is b/w july and october
5. print rainy
6. else 
7. print winter
```
* Looping constructs:
  * Lets assume we need to solve Print all the even numbers from 10 to 100
  * not a solution:
  ```
  print 10
  print 12
  print 14
  print 16
  ...
  ...
  ```
  * solution:
  ```
  index = 10
  repeat till index <= 100
    if index is even
      print index
    index = index + 1
  ```

* Is palindrome for Jarvis
```
Hi Jarvis remember the steps
Take input from user and call it a number
Jarvis can you find reverse of number and remember as reverse
if reverse is equal to number
   say palindrome
else
   say not a palindrome
```
* A Brute force approach:
```
Hi Jarvis Help me out
first = 100
second = 100
max_value = 999
max_palindrome = 0
repeat till first <= max_value
  repeat till second <= max_value
    number = first * second
    Jarvis check if the number is palindrome
    if palindrome and number > max_palindrome
      max_palindrome = number
```


#### Project Euler problem 5
* [Refer Here](https://projecteuler.net/problem=5)
* The number should be divisible by all the numbers from 1 to 20
* Solution
```
Hi Jarvis,
max_factor = 1*2*3*4......20
repeat from 20 till max_factor
   is_divisible_by_all = True
   repeat index from 1 till 20:
     if number is not divisible index
        break, 
   increment number by 20
```

### Exercise: Project Euler Problem 6
* [Refer Here](https://projecteuler.net/problem=6)

