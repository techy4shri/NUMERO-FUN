"""Command-line interface for numero-fun"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
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

def display_fancy_result(console, name, result):
    console.print(f"\n[yellow]{BORDER_LINE}[/]")
    console.print(f"""
         Name: {name}
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
        name = Prompt.ask("\n[green] Enter a name to reveal its numerology[/]")
        if not name:
            break

        result = calculate_number(name)
        display_fancy_result(console, name, result)

        response = Prompt.ask(
            "\n[italic] Would you like to try another name?[/]", 
            choices=["y", "Y", "n", "N"], 
            default="y"
        ).lower()
        
        if response in ["n", "no"]:
            break
    
    console.print(f"\n[bold purple]{BORDER_LINE}[/]")
    console.print("[bold purple] Thanks for using Numero-Fun! [/]")
    console.print(f"[bold purple]{BORDER_LINE}[/]\n")

if __name__ == "__main__":
    main()