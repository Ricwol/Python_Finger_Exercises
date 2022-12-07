# Finger exercise, p.163
# Since 1958, Canadian Thanksgiving has occurred on the second Monday in
# October.
# Write a function that takes a year (>1957) as a parameter, and returns the
# number of days between Canadian Thanksgiving and Christmas.

import calendar as cal

OCTOBER = 10
NOVEMBER = 11


def find_thanksgiving(year):
    october = cal.monthcalendar(year, OCTOBER)
    # Earliest 2nd Monday is on the 8th and latest on the 14th
    second_monday = october[1][cal.MONDAY]
    thanksgiving = second_monday if second_monday == 8 else second_monday + 7
    return thanksgiving


def days_until_christmas(year):
    """Assumes year > 1957
       Returns number of days between Canadian Thanksgiving and Christmas.
    """
    thanksgiving = find_thanksgiving(year)
    return 25 + cal.mdays[NOVEMBER] + (cal.mdays[OCTOBER] - thanksgiving)


year = int(input("Enter a year greater than 1957: "))
print(f"There are {days_until_christmas(year)} days between Thanksgiving and "
      f"Christmas in Canada in {year}.")
