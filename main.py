"""
making a numerology game
use dictionary for indexing string manipulation for iterating through name
 number game for adding
 numerology logic
"""


def get_sum(n):
    """
    Function for carry forward logic
    """
    sumi = 0
    for digit in str(n):
        sumi += int(digit)
    return sumi


# numerology function


def numero_uno(input_name):
    """
    Function for calculating the numerology of a name
    """
    alpha_dict = {
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "1",
        "k": "2",
        "l": "3",
        "m": "4",
        "n": "5",
        "o": "6",
        "p": "7",
        "q": "8",
        "r": "9",
        "s": "1",
        "t": "2",
        "u": "3",
        "v": "4",
        "w": "5",
        "x": "6",
        "y": "7",
        "z": "8",
    }
    sumi = 0
    carr = 0
    for i in input_name:
        print(i)
        if alpha_dict[i] >= 9:
            if alpha_dict[i] > 9:
                carr += get_sum(alpha_dict[i])
            else:
                continue
        else:
            sumi += int(alpha_dict[i])


# CLI DECORATION

print("*" * 10, "\n", "*" * 10)

print("NUMERO-FUN")
if __name__ == "__main__":
    name = input("Enter a name to calculate its numeral: ")
    numero_uno(name)
