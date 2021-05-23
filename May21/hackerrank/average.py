# Program to calculate the Grades
maths = int(input('Enter the marks in maths: '))
physics = int(input('Enter the marks in physics: '))
chemistry = int(input('Enter the marks in chemistry: '))
english = int(input('Enter the marks in english: '))
average = (maths + physics + chemistry + english) / 4

if average >= 90:
    print("Grade A")
elif 80 <= average < 90:
    print("Grade B")
elif 60 <= average < 80:
    print("Grade C")
elif 40 <= average < 60:
    print("Grade D")
else:
    print("Failed")
