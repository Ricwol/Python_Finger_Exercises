# Finger exercise, p.72
# Write a program that asks the user to enter an integer and prints two
# integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the
# integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

# Collect user input
x = int(input("Enter an integer: "))
# Initialize pwr to 2
pwr = 2
while pwr < 6:
    # An even exponent can't get a negative number
    if x < 0 and pwr % 2 == 0:
        # Increment pwr to an odd number
        pwr += 1
    # Initialize root for each loop to 0
    root = 0
    while root**pwr < abs(x):
        root += 1
    # Check if root, pwr pair is found
    if root**pwr == abs(x):
        break
    pwr += 1
if root**pwr != abs(x):
    print(f"There is no integer pair such that  root**pwr = {x}")
else:
    if x < 0:
        root = -root
    print(f"Integer pair found: {root}**{pwr} = {x}")
