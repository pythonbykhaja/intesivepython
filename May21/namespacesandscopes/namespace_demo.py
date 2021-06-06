course = 'python'

def change_local():
    """
    This method will change the local value
    """
    course = 'django'
    print('locals: ',locals())

def print_globals():
    """
    This method is used to print globas
    """
    print('globals: ',globals())

change_local()
print_globals()
