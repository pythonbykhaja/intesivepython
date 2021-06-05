def compound_intrest(principal, time_in_years, rate_of_intrest):
    """
    This method will compute the compound intrest
    """
    return round(principal * (( 1 + rate_of_intrest/100 ) ** time_in_years), 2)

def investment_options():
    """
    This method will return the investement options
    """
    investment_options = dict()
    investment_options['FixedDeposit'] = { 
        'State Bank of India': 5.15 , 'HDFC': 4.75 }
    investment_options['MutualFund'] = {
        'SBI Contra Fund': 14.79, 
        'Quant Tax Plan': 24.11, 
        'Canara Robeco Bluechip Equity': 18.11
        }
    investment_options['Gold']= {
        'Ornaments': 7.4,
        'ETF': 7.5
    }
    return investment_options

def propose_investment(name, principal, time_in_years):
    """
    This method summarizes all the investment options to the customer
    """
    invest_options = investment_options()
    print('Proposed by Python', end='\n\n\n')
    for option, schemes in invest_options.items():
        print(f'Exploring {option}')
        for scheme, intrest in schemes.items():
            amount_after_investment = compound_intrest(principal, time_in_years,intrest)
            print(f"This {scheme} has returns of {intrest} and your amount will be {amount_after_investment}")

        print(end='\n\n')
            



name = input('Enter your name: ')
principal = float(input('Enter the amount you want to invest: '))
time_in_years = int(input('Enter the duration for investment in years: '))
propose_investment(name, principal, time_in_years)