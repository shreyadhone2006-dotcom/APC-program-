import recursive_utils

n = int(input("Enter a number: "))

print("Factorial =", recursive_utils.factorial(n))

print("Fibonacci Series:")
for i in range(n):
    print(recursive_utils.fibonacci(i), end=" ")

print()

print("Sum of digits =", recursive_utils.sum_digits(n))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", recursive_utils.binary(n))