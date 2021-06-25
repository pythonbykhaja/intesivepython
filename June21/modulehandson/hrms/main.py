from viewmodels.operations import add_new_employee
import sys

if __name__ == '__main__':
    for place in sys.path:
        print(place)
    employees = []
    employees.append(add_new_employee())
    employees.append(add_new_employee())

    for employee in employees:
        print(employee)
    
  

