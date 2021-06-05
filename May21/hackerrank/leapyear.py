def is_leap(year):
    """
    This function determines if the year passed is leap or not

    Returns: True if leap year and false otherwise
    """
    leap = False
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            leap = False
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))