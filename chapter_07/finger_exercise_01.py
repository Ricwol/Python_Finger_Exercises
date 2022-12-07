# Finger exercise, p.163
# Write a function that meets the specification

import calendar as cal

NOVEMBER = 11


# Using find_thanksgiving function from p.163
def find_thanksgiving(year):
    month = cal.monthcalendar(year, NOVEMBER)
    if month[0][cal.THURSDAY]:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def shopping_days(year):
    """year a number >= 1941
       returns the number of days between U.S. Thanksgiving and
       Christmas in year
    """
    # Get date for Thanksgiving
    thanksgiving = find_thanksgiving(year)
    # American Christmas on the 25th of December
    # Subtract date for Thanksgiving from total number of days in November
    return (cal.mdays[NOVEMBER] - thanksgiving) + 25


year = int(input("Enter a year greater or equal 1941: "))
print(f"There are {shopping_days(year)} days between Thanksgiving and "
      f"Christmas in {year}.")
