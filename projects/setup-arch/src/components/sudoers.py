"""
This file will handle the creating of the sudoers file.
"""

# Imports
import os
from system import System

# Sudoers class
class Sudoers:
    def __init__(self):
        raise Exception("This class cannot be instantiated.")

    @staticmethod
    def create(Printer) -> None:
        """
        Creates the sudoers file.
        """
        # Create the sudoers file
        System.call("cp /etc/sudoers /etc/sudoers.bak")

        # Get the template file
        template = System.readFile(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "template_files", "sudoers.txt")))

        # Write the template to the sudoers file
        with open("/etc/sudoers", "w") as file:
            file.write(template)

        # Print a success message
        Printer.log(Printer.format("✅\tSudoers created!", colour="green"))