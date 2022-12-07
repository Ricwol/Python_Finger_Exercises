# Finger exercise, p.148
# The harmonic sum of an integer, n > 0, can be calculated using the formula
# 
# harmonic sum = 1 + 1/2 + ... + 1/n
#
# Write a recursive function that computes this.

def harmonic_sum(n):
    """Returns the harmonic sum for n > 0
    """
    # Base case when n is 1
    if n == 1:
        return n
    # Harmonic sum for all other natural numbers
    return 1/n + harmonic_sum(n-1)


# Harmonic sum for n=10 is around 2.92896825396825396825...
print(harmonic_sum(10))
