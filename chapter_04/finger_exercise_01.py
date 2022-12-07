# Finger exercise, p.93
# Use the find_root function in Figure 4-3 to print the sum of approximations
# to the square root of 25, the cube root of -8, and the fourth root of 16.
# Use 0.001 as epsilon.

def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        # Negative number has no even-powered roots
        return None
    # Catch values -1 < x < 1
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high+low) / 2

    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low) / 2
    return ans

values = ((25, 2), (-8, 3), (16, 4))
epsilon = 0.001
total = 0
for num, pwr in values:
    ans = find_root(num, pwr, epsilon)
    print(f"{num}**{pwr} = {ans}")
    if ans is not None:
        total += ans

print(f"Sum of approximations: {total}")
