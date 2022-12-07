# Finger exercise, p.79
# What would have to be changed to make the code in Figure 3-5 work for
# finding an approximation to the cube root of both negative and positive
# numbers?
# Hint: think about changing low to ensure that the answer lies within the
# region being searched.

# The following parts must be changed to approximate the cube root:
# 1. Initialization of low from low = 0 to low = min(-1, x) to include
#    negative values of x < -1 and values -1 < x < 0
# 2. The test condition of the while loop from ans**2 to ans**3
# 3. The if condition from ans**2 < x to ans**3 < x for changing the upper or
#    lower bound for the next calculation of ans of the bisection search

x = float(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0
# Set low to -1 if -1 < x < 0, otherwise x
low = min(-1, x)
# If 0 < x < 1 set high to 1, x otherwise
high = max(1, x)
ans = (high+low) / 2
# Change quadratic exponent to cube
while abs(ans**3 - x) >= epsilon:
    print(f"{low = } {high = } {ans = }")
    num_guesses += 1
    # Change upper or lower bound depending if ans**3 is greater x or less
    if ans**3 < x:
        low = ans
    else:
        high = ans
    # Calculate new middle value
    ans = (high+low) / 2
print(f"number of guesses = {num_guesses}")
print(f"{ans} is close to cube root of {x}")
