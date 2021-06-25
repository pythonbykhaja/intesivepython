from models.models import Employee
from utilities.utils import * 
from viewmodels.testing import is_even, is_prime

def add_new_employee():
    """
    This method should add the new employee
    by asking the inputs from users
    """
    is_prime()
    name = get_input('Employee Name')
    id = get_input('id')
    dept = get_input('department')
    email_id = get_input('Email id')
    mobile_no = get_input('mobile number')
    emp = Employee(name,id,dept,email_id, mobile_no)
    return emp
    