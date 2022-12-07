# Finger exercise, p.95
# Write a function mult that accepts either one or two ints as arguments.
# If called with two arguments, the function prints the product of the two
# arguments.
# If called with one argument, it prints that argument.

def mult(num1, num2=None):
    if num2 is None:
        print(num1)
    else:
        print(f"{num1} * {num2} = {num1 * num2}")
