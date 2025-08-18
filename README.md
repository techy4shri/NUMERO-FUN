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

- Calculate the numerology of a given name
- User-friendly command-line interface with rich formatting
- Supports both uppercase and lowercase input
- Multiple calculation modes

## Installation

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

result = calculate_number("john")
print(result)  # Output: 2
```

### Example Output
```
╭──────────────────────────────────────────────────╮
│               NUMERO-FUN CALCULATOR              │
╰──────────────────────────────────────────────────╯

Enter a name to calculate its numeral: john
╭──────────────────────────────────────────────────╮
│ Name: garima                                     │
│ Your Number: 4                                   │
╰──────────────────────────────────────────────────╯
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

This project is licensed under the GPL-3.0 Licence , more info in [LICENCE.md]()
