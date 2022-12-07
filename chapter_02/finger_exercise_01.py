# Finger exercise, p.54
# Write code that asks the user to enter their birthday in the form
# mm/dd/yyyy, and then prints a string of the form
# ‘You were born in the year yyyy.’

birthday = input("Ener your birthday in the form mm/dd/yyyy: ")
# Use f-string and slicing with negative index to get the last 4 characters
print(f"You were born in the year {birthday[-4:]}.")
