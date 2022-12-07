# Finger exercise, p.166
# Write a program that first stores the first ten numbers in the Fibonnaci
# sequence to a file named fib_file. Each number should be on a separate line
# in the file.
# The program should then read the numbers from the file and print them.

filename = "fib_file"

with open(filename, "w") as fh:
    a, b = 0, 1
    for _ in range(10):
        a, b = b, a+b
        fh.write(str(a) + "\n")

print(f"Read first 10 Fibonacci numbers from file {filename!r}:")
with open(filename) as fh:
    for line in fh:
        print(line.rstrip())
