# Finger exercise, 128
# Write a list comprehension that generates all non-primes between 2 and 100.

# Get all primes between 2 and 100
# List comprehension for primes, p.128 has an error
primes = [prime for prime in range(2, 100) 
          if all(prime % x != 0 for x in range(2, prime))]

# Get all non-primes between 2 and 100
non_primes = [num for num in range(2, 100)
              if any(num % x == 0 for x in range(2, num))]

# Test if primes and non_primes have no value in common
duplicates = [n for n in non_primes if n in primes]

print(f"{primes     = }")
print(f"non-primes = {non_primes}")
print(f"{duplicates = }")
