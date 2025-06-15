# Leap year or not

def is_leap_year(year):
    """
    Enter a year and check if it is a leap year or not.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap_year(2020)  # True
# hover over the function name to see the docstring