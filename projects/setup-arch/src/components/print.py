"""
This file handles all printing related tasks.
"""


from system import System

class Printer:
    """
    A class to handle printing to the console.
    """
    Colours: dict[str, int] = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
    }

    FontWeights: dict[str, int] = {
        "normal": 39,
        "bold": 1,
        "dim": 2,
        "italic": 3,
        "underline": 4,
        "blink": 5,
        "reverse": 6,
        "hidden": 7,
    }

    @staticmethod
    def log(msg: str) -> None:
        """
        Logs a message to the console.

        :param msg: The message to log.
        """
        print(msg)

    @staticmethod
    def empty() -> None:
        """
        Prints an empty line.
        """
        print("")

    def header() -> None:
        """
        Generates and prints a header in the console.
        """

        # Get the header
        header = Printer.generateHeader()

        # Print the header
        Printer.log(header)

        # Return
        return

    @staticmethod
    def generateHeader() -> str:
        """
        Generates a header.

        :return: The generated header.
        """

        # Get the width
        width = int(System.call_output("tput cols"))

        # Get the header
        header = "=" * width

        # Add text to the header
        header += "\n"
        header += Printer.format("Welcome To The Arch Setup!", colour="magenta", weight="bold").center(width)
        header += "\n"
        header += ("=" * width)

        # Return
        return header
    
    @staticmethod
    def format(text: str, colour: str = "white", weight: str = "normal") -> str:
        """
        Takes text and formats it.
        """

        # Get the colour
        colour = Printer.Colours.get(colour, 38)

        # Get the weight
        weight = Printer.FontWeights.get(weight, 39)

        # Split the text
        text = " ".join([s.title() for s in text.split()])

        # Format the text
        formatted_text = f"\033[{weight};{colour}m{text}\033[0m"

        # Return
        return formatted_text