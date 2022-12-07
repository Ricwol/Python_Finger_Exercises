# Finger exercise, p.243
# What is the asymptotic complexity of each of the following instructions?

def g(L, e):
    """L a list of ints, e is an int"""
    for i in range(100):  # This is constant time
        for e1 in L:  # This is of time len(L) at worst and 1 at best
            if e1 == e:
                return True
    return False

# The number of steps in g() is: 100 * len(L)
# Let's say list L is of size n, giving us 100*n.
# As per rules we can neglect multiplicative constant factors.
# This gives us an asumptotic complexity for g() order of O(n)


def h(L, e):
    """L a list of ints, e is an int"""
    for i in range(e):  # This is of time e
        for e1 in L:  # This is of time len(L)=n at worst and 1 at best
            if e1 == e:
                return True
    return False

# The number of steps in h() is e*len(L).
# Let's say list L is of size n.
# The worst case has e not in list.
# This gives us an asymptotic complexity for h() order of O(e*n)
