# Finger exercise, p.58
# Write a program that asks the user to input 10 integers, and then prints
# the largest odd number that was entered. If no odd number was entered, it
# should print a message to that effect.

# Initialize odd_num with None as no odd number was given yet
odd_num = None

num_iterations = 0
# Set while condition to literal 10 to collect 10 numbers from user
while num_iterations < 10:
    x = int(input("Enter a number: "))
    # Check if user input is odd
    if x % 2 != 0:
        # Using conditional expression to determin largest odd number
        odd_num = x if odd_num is None else max(x, odd_num)
    num_iterations += 1

# odd_num remains None if only even numbers are entered
if odd_num is None:
    print("No odd numbers entered.")
else:
    print(f"The largest odd number entered is: {odd_num}")
