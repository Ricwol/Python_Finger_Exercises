# Finger exercise, Figure 3-7, p.85
# Add some code to the implementation of Newton–Raphson that keeps track of the
# number of iterations used to find the root. Use that code as part of a
# program that compares the efficiency of Newton–Raphson and bisection search.
# (You should discover that Newton–Raphson is far more efficient.)

# Newton-Raphson approximation for square root
# Find x such that x**2 - k is within epsilon of 0
k = float(input("Enter a number: "))
epsilon = 0.01
guess = k / 2
num_guesses = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - ((guess**2 - k) / (2*guess))
    num_guesses += 1
print(f'Square root of {k} is about {guess}')
print(f"Newton-Raphson: {num_guesses} guesses.")

low = 0
high = max(k, 1)
guess = (high+low) / 2
num_guesses = 0
while abs(guess**2 - k) >= epsilon:
    if guess**2 < k:
        low = guess
    else:
        high = guess
    guess = (high+low) / 2
    num_guesses += 1
print(f"Square root of {k} is about {guess}")
print(f"Bisection Search: {num_guesses} guesses.")
