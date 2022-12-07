# Finger exercise, p.72
# Change the code in Figure 3-2 so that it returns the largest rather than the
# smallest divisor. Hint: if y*z = x and y is the smallest divisor of x, z is
# the largest divisor of x.

# Collect user input, assume user enters only integer greater than 2
x = int(input("Enter an integer greater than 2: "))
# Set largest_divisor to None
largest_divisor = None
for guess in range(x-1, 1, -1):
    if x % guess == 0:
        largest_divisor = guess
        break
if largest_divisor is not None:
    print(f"Largest divisor of {x} is {largest_divisor}")
else:
    print(f"{x} is a prime number")
