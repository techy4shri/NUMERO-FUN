"""Core numerology calculation functions"""

def letter_to_number(letter):
    if not letter.isalpha():
        return 0
    number = ord(letter.lower()) - ord('a') + 1
    return ((number - 1) % 9) + 1

def get_sum(n):
    return sum(int(digit) for digit in str(n))

def calculate_number(input_name):
    sum_total = sum(letter_to_number(char) for char in input_name.lower())
    while sum_total > 9:
        sum_total = get_sum(sum_total)
    return sum_total