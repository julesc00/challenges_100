"""
2.1.3 Short Introduction to Prime Numbers

    A prime number is a natural number that is greater than 1 and exclusively divisible by
    itself and by 1. There are two quite understandable algorithms for checking whether a
    given number is prime or for calculating primes up to a given maximum value.

    Brute force algorithm for prime numbers Whether a number is a prime number or
    not can be determined as follows. You look for the number to be checked starting from 2
    up to at most half of the number, whether the current number is a divisor of the original
    number.2 In that case, it’s not a prime.
"""


def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2+1):
        if potentially_prime % i == 0:
            return False
    return True


PRIMES = []
for number in range(2, 25):
    if is_prime(number):
        PRIMES.append(number)

print(PRIMES)

PRIMES2 = [number for number in range(2, 25) if is_prime(number)]
print(PRIMES2)
