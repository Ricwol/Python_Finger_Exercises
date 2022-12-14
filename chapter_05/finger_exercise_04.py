# Finger exercise, p.130
# Implement a function satisfying the following specification.
# Hint: it will be convenient to use lambda in the body of the implementation.

def f(L1, L2):
    """L1, L2 lists of same length of numbers
       returns the sum of raising each element in L1 to the power of the
       element at the same index in L2
       For example, f([1,2], [2,3]) returns 9
    """
    # Using sum and map
    # return sum(map(lambda x,y: x**y, L1, L2))

    # Using list comprehension instead of map
    return sum([x**y for x, y in zip(L1, L2)])


print(f([1, 2], [2, 3]))
