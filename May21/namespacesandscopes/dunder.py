def exploring():
    """
    This function is created for exploring dunder variables
    """
    print(f"Name of this function is {exploring.__name__}")
    print(f"And its documentation is {exploring.__doc__}")

print(f'globals: ', globals())
exploring()