"""Core numerology calculation functions"""

def letter_to_number(letter):
    """Modern numerology: A=1, B=2, ..., I=9, J=1, etc."""
    if not letter.isalpha():
        return 0
    number = ord(letter.lower()) - ord('a') + 1
    return ((number - 1) % 9) + 1

def letter_to_chaldean(letter):
    """Chaldean numerology: Uses 1-8 with specific letter mappings"""
    chaldean_map = {
        'a': 1, 'i': 1, 'q': 1, 'j': 1, 'y': 1,
        'b': 2, 'k': 2, 'r': 2,
        'c': 3, 'g': 3, 'l': 3, 's': 3,
        'd': 4, 'm': 4, 't': 4,
        'e': 5, 'h': 5, 'n': 5, 'x': 5,
        'u': 6, 'v': 6, 'w': 6,
        'o': 7, 'z': 7,
        'f': 8, 'p': 8 
    }
    return chaldean_map.get(letter.lower(), 0)

def letter_to_pythagorean(letter):
    """Pythagorean numerology: Preserves master numbers 11, 22, 33"""
    if not letter.isalpha():
        return 0
    number = ord(letter.lower()) - ord('a') + 1
    base = ((number -1)%9)+1
    return base

def get_sum(n):
    """Simple digit sum"""
    return sum(int(digit) for digit in str(n))

def get_pythagorean_sum(n):
    """Preserves master numbers 11, 22, 33"""
    if n in [11, 22, 33]:
        return n
    return get_sum(n)

def calculate_number(input_name, method ='modern'):
    """Calculate numerology number using specified method"""
    methods = {
        'modern': letter_to_number,
        'chaldean': letter_to_chaldean,
        'pythagorean': letter_to_pythagorean
    }

    letter_func = methods.get(method, letter_to_number)
    sum_func = get_pythagorean_sum if method == 'pythagorean' else get_sum
    sum_total = sum(letter_func(char) for char in input_name.lower())
    while sum_total > 9 and (method != 'pythagorean' or sum_total not in [11, 22, 33]):
        sum_total = sum_func(sum_total)
    return sum_total