from viewmodels.operations import add_new_employee

if __name__ == '__main___':
    employees = []
    employees.append(add_new_employee())
    employees.append(add_new_employee())

    for employee in employees:
        print(employee)
    
  

