def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def armstrong(n):
    digits = str(n)
    total = 0

    for digit in digits:
        total += int(digit) ** len(digits)

    return total == n


def palindrome(n):
    return str(n) == str(n)[::-1]