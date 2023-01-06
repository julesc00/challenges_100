"""
    Extraction of digits To extract the digits of a number, combine modulo and division
    as long as the remaining value is greater than 0.

    Results for 123 are printed in reverse order.
    """


def extract_digits1(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value //= 10
        print(digit, end=" ")


def extract_digits2(number):
    """
    Example 2
    divmod(), which returns both the divisor and the remainder as a result—as a shortcut for the operators
    that are often called in combination.
    """
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=" ")


def count_digits(number):
    """
    Determine number of digits Instead of extracting individual digits, you can also use
    a repeated division to determine the number of digits in a decimal number by simply
    dividing by 10 until there is no remainder left
    """
    count, remaining_value = 0, number
    while remaining_value > 0:
        remaining_value //= 10
        count += 1
    return count


if __name__ == "__main__":
    extract_digits1(123)
    print()
    extract_digits2(123)
    print()
    print(count_digits(123))
