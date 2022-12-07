# Finger exercise, p.108
# Write a lambda expression that has two numeric parameters. If the second
# argument equals zero, it should return None. Otherwise it should return the
# value of dividing the first argument by the second argument.
# Hint: use a conditional expression.

div = lambda x, y: x/y if y != 0 else None

test_vals = ((56, 7), (3, 4), (0, 2), (3, 2), (9, 0))
for x, y in test_vals:
    print(f"{x}/{y} = {div(x, y)}")
