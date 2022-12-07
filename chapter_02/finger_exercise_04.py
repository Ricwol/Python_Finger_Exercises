# Finger exercise, p.62
# Write a program that prints the sum of the prime numbers greater than 2 and
# less than 1000.
# Hint: you probably want to use a for loop that is a primality test nested
# inside a for loop that iterates over the odd integers between 3 and 999.

primes_sum = 0
# Loop through range with start=3, stop=1000 and step=2
# Set step=2 as all even numbers are divisible by 2 and therefore not prime
for prime in range(3, 1000, 2):
    # Primality test checks all numbers from 3 up to prime-1
    for n in range(3, prime):
        # Check if prime is actually a prime
        if prime % n == 0:
            # Set value to 0 as it is not a prime number
            prime = 0
            # Break inner for loop as primality test found not prime
            break
    # Sum all primes greater than 2 and less than 1000
    primes_sum += prime

print(primes_sum)
