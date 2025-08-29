"""
making a numerology game
using modular arithmetic for letter-to-number conversion

This file is just for testing purposes. The old but starting point of this all
"""


def letter_to_number(letter):
    """
    Convert letter to numerology number (1-9)
    Using the pattern: A=1, B=2, C=3, ..., I=9, J=1, K=2, etc.
    Using a trick to get the letter's number instead of dict
    Nothing fancy just age old modulo
    """
    if not letter.isalpha():
        return 0

    number = ord(letter.lower()) - ord("a") + 1
    # Convert to 1-9 pattern using modulo
    return ((number - 1) % 9) + 1


def get_sum(n):
    """
    Function for carry forward logic
    """
    sum_i = 0
    for digit in str(n):
        sum_i += int(digit)
    return sum_i


def numero_uno(input_name):
    """
    Function for calculating the numerology of a name.
    Returns the final single digit number.
    """
    sum_total = 0

    for char in input_name.lower():
        sum_total += letter_to_number(char)

    while sum_total > 9:
        sum_total = get_sum(sum_total)

    return sum_total


# CLI DECORATION
print("*" * 10, "\n", "*" * 10)
print("NUMERO-FUN")

if __name__ == "__main__":
    name = input("Enter a name to calculate its numeral: ")
    result = numero_uno(name)
    print(f"The numerology number for {name} is: {result}")
