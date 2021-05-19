### Sequence: Basic Building Blocks of Program
* The concept of sequence is to decide what steps a program will perform to accomplish its overall task
* Lets try to list out the steps to get the tea
  * Ensure we have milk, tea powder, sugar, water and stove
  * add milk, water, tea powder in a bowl and heat it on the stove
  * Wait till the tea is prepared 
  * From bowl filter the tea and pour into cups
  * serve the tea in cups

#### Project Euler 3
* For problem [Refer Here](https://projecteuler.net/problem=3)
* Lets try to write sequence of steps
```
1. Get the number
2. Try to find the largest factor
3. Check if the factor is prime
4. if the factor is prime print the number and stop the program
5. else go to step 2 to find the next largest factor
```
* Lets speak with Jarvis to find the prime number
```
Hi Jarvis, Remember the steps to find the value is prime or not
start with index=2 till index < value//2
   if value%index == 0
      then say not prime and exit
    increment index by 1

say prime

```
* Now lets get the sequence solved by Jarvis
```
Hi Jarvis can you help me out
Remember input from user as value
start with index = value//2 till index > 2
   if value%index == 0 
      then say index is largest factor
      ask jarvis to check if it prime
      if jarvis say its prime print the index and exit
   decrement index by 1
```

#### Problem
* Try to find if the number is palindrome or not
```
123 => 321
353 => 353
```
* Sequence
```
1. Take input from user and call it as number
2. calculate the reverse of the number and call it as reverse
3. if reverse is equal to number then say number is palindrome else not a palindrome
```
* Lets Speak with Jarvis to find a reverse of a number
```
Hi Jarvis, Remember the steps to find the reverse of value
remember result with value 0
repeat till value is equal to 0
   calculate value%10 and remember as remainder
   calculate result*10 and remember as result
   add remainder to result
   calculate value//10 and remember as value
say reverse
```
* Lets find the number is palindrome or not by Jarvis
```
Hi Jarvis help me out
Take input from user and call it a number
Jarvis can you find reverse of number and remember as reverse
if reverse is equal to number
   say palindrome
else
   say not a palindrome
```

#### Problem
* Statement: Find the sum of squares of all the numbers
```
# Example 1
input: 5
1*1 + 2*2 + 3*3 + 4*4 + 5*5

input 6
1*1 + 2*2 + 3*3 + 4*4 + 5*5 + 6*6
```
* sequence
```
Take input from user as value
calculate square of each number from 1 to value 
show the result
```
* Lets speak with Jarvis
```
Remember input as value
Remember 1 as index
Remember 0 as result
repeat till index is equal to or less than value
    calculate index*index and add it to result
    increment index by 1
say result
```


### Data Types in Programming Languages
* While programming we might need to store the value in the memory (RAM), Datatype represents two things
  * RAM => How much memory is need to store this
  * User => What is type of the data which needs to be memorized
* Datatypes help in allocating the memory and that memory location is referred by a variable or constant
```
int index = 100;
```
* Naming Variables
  * Pascal Casing:
  ```
  FirstName
  EmailAddress
  PinCode
  ```
  * Camel Casing
  ```
  firstName
  emailAddress
  pinCode
  ```
  * snake case
  ```
  first_name
  email_address
  pin_code

  ```
* Whenever we want define variable, ensure meaningful names are give
```
index
message
```
* Primitive DataTypes: These are types of data which can handle a single value
  * Boolean
  * Numeric types
    * integer 
    * floating point number
  * Text/Characters (String) 


