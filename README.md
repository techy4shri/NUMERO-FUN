# README.md

# Numerology CLI Tool
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗  ██████╗ 
                    ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔═══██╗
                    ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║   ██║
                    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║
                    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝
                    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝

                                ███████╗██╗   ██╗███╗   ██╗
                                ██╔════╝██║   ██║████╗  ██║
                                █████╗  ██║   ██║██╔██╗ ██║
                                ██╔══╝  ██║   ██║██║╚██╗██║
                                ██║     ╚██████╔╝██║ ╚████║
                                ╚═╝      ╚═════╝ ╚═╝  ╚═══╝
                                    ┬┌─┐  ┬ ┬┌─┐┬─┐┌─┐┬
                                    │└─┐  ├─┤├┤ ├┬┘├┤ │
                                    ┴└─┘  ┴ ┴└─┘┴└─└─┘o
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
This project is a command-line interface (CLI) tool for calculating the numerology of a name. It started as a practice project for dictionary and OOPS concepts in python but since the dictionary was getting quite lengthy and inefficient (kinda annoying too), I replaced it with a classic modulo math trick :D

## Features

- Calculate the numerology of a given name using three different methods:
  - Modern (Standard numerology 1-9)
  - Chaldean (Ancient system 1-8)
  - Pythagorean (Preserves master numbers 11, 22, 33)
- Interactive method selection using arrow keys
- User-friendly command-line interface with rich formatting
- Supports both uppercase and lowercase input
- Error handling and input validation

## Installation

### Development Version
```bash
git clone https://github.com/techy4shri/Numero-Fun.git
cd Numero-Fun
pip install -e .
```

### From PyPI
```bash
pip install numero-fun
```

### From Source
```bash
git clone https://github.com/yourusername/Numero-Fun.git
cd Numero-Fun
pip install .
```

## Usage

There are three ways to use this tool:


### 1. Command Line Tool (Recommended)
```bash
numero-fun
```

### 2. Python Module
```bash
python -m numero_fun.cli
```

### 3. Python Package
```python
from numero_fun import calculate_number

result = calculate_number("shri")
print(result)

chaldean_result = calculate_number("john", method="chaldean")
pythagorean_result = calculate_number("john", method="pythagorean")
```

### Example Output
```
╭──────────────────────────────────────────────────╮
│           NUMERO-FUN CALCULATOR                  │
╰──────────────────────────────────────────────────╯

Choose numerology method:
❯ Modern         - Standard numerology (1-9)
  Chaldean       - Ancient system (1-8)
  Pythagorean    - Preserves master numbers

Enter a name to calculate its numeral: SHRI
╭──────────────────────────────────────────────────╮
│ Name: SHRI                                       │
│ Method: Standard numerology (1-9)                │
│ Your Magical Number is: 9                        │
╰──────────────────────────────────────────────────╯

Would you like to try another name? (y/n)
```

## Development

To set up the development environment:

```bash
git clone https://github.com/yourusername/Numero-Fun.git
cd Numero-Fun
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to:
- Submit a pull request for different numerological calculation logics
- Open an issue if you find a bug
- Suggest new features or improvements

## License

This project is licensed under the GPL-3.0 Licence , more info in [LICENCE.md](https://github.com/techy4shri/NUMERO-FUN/blob/main/LICENSE)
