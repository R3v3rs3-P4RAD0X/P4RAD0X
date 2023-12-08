"""
System.py

This file will handle running system commands.
"""

# Imports
import os
import sys


class System:
    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated.")

    @staticmethod
    def call(command: str) -> bool:
        """
        Runs a system command.

        :param command: The command to run.
        """
        # Run command
        return os.system(command) == 0

    @staticmethod
    def call_output(command: str) -> str:
        """
        Runs a system command and returns the output.

        :param command: The command to run.
        :return: The output from the command.
        """
        # Run command
        return os.popen(command).read().strip()
    
    @staticmethod
    def readFile(path: str) -> str:
        """
        Reads a file and returns the contents.

        :param path: The path to the file.
        :return: The contents of the file.
        """
        # Open the file
        with open(path, "r") as file:
            # Return the contents
            return file.read()