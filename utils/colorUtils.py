"""
Color utilities for printing colored text to the terminal.
"""

from dataclasses import dataclass


@dataclass
class Color:
    """A class for storing color data as ANSI escape codes."""
    none: str = "\033[0m"
    black: str = "\033[30m"
    red: str = "\033[31m"
    green: str = "\033[32m"
    yellow: str = "\033[33m"
    blue: str = "\033[34m"
    magenta: str = "\033[35m"
    cyan: str = "\033[36m"
    white: str = "\033[37m"


def cprint(text: str, color: str):
    """
    Prints text in a specified color.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in as an ANSI color code.
    """
    print(f"{color}{text}{Color.none}")


def highlight(text: str, substring: str, color: str):
    """
    Highlights a substring in a string.

    Args:
        text (str): The text to highlight the substring in.
        substring (str): The substring to highlight.
        color (str): The color to highlight the substring in as an ANSI color code.

    Returns:
        str: The text with the substring highlighted.
    """
    return text.replace(substring, f"{color}{substring}{Color.none}")


def hprint(text: str, substring: str, color: str):
    """
    Prints text with a substring highlighted.

    Args:
        text (str): The text to print.
        substring (str): The substring to highlight.
        color (str): The color to highlight the substring in as an ANSI color code.
    """
    print(highlight(text, substring, color))
