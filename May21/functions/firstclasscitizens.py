from datetime import date

def pm_plain(message):
    print(message)

def pm_log_format(message):
    import datetime
    print(f"{datetime.datetime.now()}  {message}")

def pm_dictionary_format(message):
    import datetime
    message_dict = {'time': datetime.datetime.now(), 'message': message}
    print(message_dict)

def make_a_choice():
    choice = input('Enter p for plain, l for log and d for dict ')
    print_format = None
    if choice == 'p':
        print_format = pm_plain
    elif choice == 'l':
        print_format = pm_log_format
    else:
        print_format = pm_dictionary_format
    return print_format


pf = make_a_choice()
for index in range(1,10000):
    pf(index)




