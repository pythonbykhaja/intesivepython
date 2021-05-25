# This program responds to user by accepting the number and determines
# whether the number is even or odd

while True:
    number = int(input('Enter the number: '))
    if number%2 ==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    # Now the program needs to ask user whether he wants to continue
    user_option = input(
        'Do you want to continue? [type y to continue and n to stop]')
    if user_option == 'n':
        break
print('Thanks for using our program')