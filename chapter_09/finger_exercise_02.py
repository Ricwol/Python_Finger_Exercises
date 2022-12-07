# Finger exercise, p.197
# Implement a function that satisfies the specification

def find_an_even(L: list) -> int:
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number
    """
    for num in L:
        try:
            # Returns the first even number found in L
            if num % 2 == 0:
                return num
        except TypeError:
            pass
    # Raises an error when no even numbers are given
    raise ValueError("List doesn't contain an even number.")


print(int("c"))
print(f"Even number found: {find_an_even([1, 'a', 3, 2])}")
print(f"No even number here: {find_an_even([i for i in range(1, 10, 2)])}")
