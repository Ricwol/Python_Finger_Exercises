# Finger exercises, p.192
# Implement a function that meets the specification below.
# Use a try-except block. Hint: before starting to code, you might want to
# type something like 1 + 'a' into the shell to see what kind of exception is
# raised.

def sum_digits(s: str) -> int:
    """Returns the sum of the decimal digits in s

       For example, if s is 'a2b3c' it returns 5
    """
    total = 0
    for c in s:
        try:
            digit = int(c)
        except ValueError:
            # Skip current character as it is not numerical
            continue
        else:
            total += digit
    return total


print(f"total: {sum_digits('a')}")
print(f"total: {sum_digits('a2b3c')}")
print(f"total: {sum_digits('123')}")
