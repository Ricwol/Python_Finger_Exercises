# Finger exercise, p.58
# Replace the comment in the following code with a while loop.

# Collect user input
n = int(input("How many times should I print the letter X? "))
# Initialize to_print as empty string
to_print = ""
# Loop as long as the condition is True
while n > 0:
    # Concatenate 'X' to to_print n times
    to_print += "X"
    # Decrement n by 1
    n -= 1
print(to_print)
