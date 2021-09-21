def simple_interest(principal, time, rate):
    """
    This function calculates the simple interest
    """
    return (principal * time * rate)/100


def compound_interest(principal, time, rate):
    """
    This function returns compound interest
    """
    return principal * ( 1 + (rate/100))**time

def investment_options():
    principal = float(input("Enter the amount: "))
    time = int(input("Enter the investment period in years: "))
    rate = float(input("Enter the rate of interest: "))
    si = simple_interest(principal,time, rate)  
    ci = compound_interest(principal, time, rate)
    print(f"Amount after 5 years with Simple interest is {principal+si} \nCompund interest is {ci:.2f}")



while True:
    investment_options()
    choice = input("Enter N to quit, any other key to continue")
    if choice == 'N':
        break

