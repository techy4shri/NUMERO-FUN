"""Command-line interface for numero-fun"""
from .calculator import calculate_number

def main():
    print("*" * 10)
    print("NUMERO-FUN")
    print("*" * 10)
    
    name = input("Enter a name to calculate its numeral: ")
    result = calculate_number(name)
    print(f"The numerology number for {name} is: {result}")

if __name__ == "__main__":
    main()