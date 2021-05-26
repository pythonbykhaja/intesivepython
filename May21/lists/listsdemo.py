# How do you represent the following data in python (covered so far)

#| name| phone num| Qual|
#|-----|----------|------|
#| ram | 99999999 | BTech |
#| shyam | 8888888 | MTech |
#| sita | 77777777 | MCA |
#| geeta | 6666666 | BSc |

students_list = []

while True:
    name = input("Enter Student's name: ")
    phone_number = input("Enter Student's contact number: ")
    qualification = input("Enter Student's qualification: ")
    student = [ name, phone_number, qualification,]
    students_list.append(student)
    choice = input("Do you want to continue? [Press y to continue and n to exit]")
    if choice == 'n':
        break