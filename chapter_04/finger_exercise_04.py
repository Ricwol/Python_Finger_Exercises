# Finger exercise, p.105
# Using the algorithm of Figure 3-6, write a function that satisfies the 
# specification: 

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
            x > 1, epsilon > 0 and base >= 1
        Returns float y such that base**y is within epsilon of x.
    """
    # Assumption not met
    if x <= 1 or epsilon <= 0 or base < 1:
        return

    # Algorithm of Figure 3-6, p.79 of log base 2
    # Find lower bound on ans
    lower_bound = 0
    # Change pecific case with base 2 to general case base
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (high+low) / 2

    # Change specific case to general case base
    while abs(base**ans - x) >= epsilon:
        # Change specific case to general case base
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high+low) / 2
    return ans
