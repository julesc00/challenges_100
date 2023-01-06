"""
2.1.2 Short Introduction to Divider

    In the following, you examine how to determine all real divisors of a number (i. e., those
    without the number itself ). The algorithm is quite simple. Initially, the result contains
    the number 1, as this is always a valid divider. Then you go through all numbers starting
    by 2 up to half of the value (all higher values cannot be integer divisors if 2 is already
    a divisor) and check if they divide the given number without a remainder. If this is the
    case, then this number is a divisor and is included in a result list.
"""


def find_proper_divisors1(value):
    divisors = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


def find_proper_divisors2(value):
    # Same as above, with list comprehension
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


if __name__ == "__main__":
    print(find_proper_divisors1(99))
    print(find_proper_divisors2(103))
