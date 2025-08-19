"""Command-line interface for numero-fun"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
import questionary
from .calculator import calculate_number


ASCII_HEADER = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

BORDER_LINE = "═══════════════════════════════════════════"
SIDE_BORDER = "║"

COLORFUL_THEME = {
    'header': 'bold yellow',
    'prompt': 'green',
    'result': 'bold cyan',
    'border': 'bright_green',
    'accent': 'yellow',
    'exit': 'bold purple'
}

def is_valid_input(name):
    """Checks if the input name is valid (non-empty and alphabetic)."""
    return all(char.isalpha() or char.isspace() for char in name)

def display_fancy_result(console, name, result, method):
    """Display the numerology result in pretty format."""
    method_descriptions = {
        "modern": "Standard numerology (1-9)",
        "chaldean": "Ancient system (1-8)",
        "pythagorean": "Preserves master numbers aka 11,22,33"
    }
    console.print(f"\n[yellow]{BORDER_LINE}[/]")
    console.print(f"""
         Name: {name}
         Method: {method_descriptions.get(method.lower(), "Unknown Method")}
         Your Magical Number is: {result}
    """)
    console.print(f"\n[yellow]{BORDER_LINE}[/]")

def main():
    console = Console(theme=Theme(COLORFUL_THEME))
    console.print(f"[bold yellow]{ASCII_HEADER}[/]")
    
    console.print(Panel.fit(
        "[bold yellow] Your Mystical Numerology Calculator [/]",
        border_style="bright_green",
        padding=(1, 2)
    ))



    while True:
        method = questionary.select(
            "\n[cyan] Choose numerology method[/]",
            choices=[
                "Modern - Standard numerology (1-9)",
                "Chaldean - Ancient system (1-8)",
                "Pythagorean - Preserves master numbers aka 11,22,33"
            ],
            use_indicator=True,
            use_shortcuts=True
        ).ask()
        method = method.split(" - ")[0].strip().lower()

        name = Prompt.ask("\n[bold cyan] Enter a name to reveal its numerology[/]")
        if not name:
            raise KeyboardInterrupt
        if not is_valid_input(name):
            console.print("[bold red] Error: Please enter a valid input[/]")
            continue

        result = calculate_number(name, method)
        display_fancy_result(console, name, result, method)

        response = Prompt.ask(
            "\n[italic] Would you like to try another name?[/]", 
            choices=["y", "Y", "yes", "Yes", "n", "N", "no", "No"],
            show_choices=False,
            default="y"
        ).lower()

        if response in ["n", "N", "no", "No"]:
            break
    
    console.print(f"\n[bold purple]{BORDER_LINE}[/]")
    console.print("[bold purple] Thanks for using Numero-Fun! [/]")
    console.print(f"[bold purple]{BORDER_LINE}[/]\n")

if __name__ == "__main__":
    main()