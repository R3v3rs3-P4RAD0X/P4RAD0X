"""
System.py

This file will handle running system commands.
"""

import configparser

# Imports
import os
import re
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

    @staticmethod
    def readConfig() -> dict:
        """
        Reads the config file and returns the contents.

        :return: The contents of the config file.
        """
        # Get the path to the config file
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))

        # Create a config parser
        parser = configparser.ConfigParser()

        # Read the config file
        parser.read(path)

        # Create a dictionary for config
        config = {}

        # Iterate over the sections
        for section in parser.sections():
            # Iterate over the options
            for option in parser.options(section):
                # Get the value
                value = parser.get(section, option)

                # Split by any spaces
                value = value.split(" ")[0]

                # Check if the value is a boolean
                if value.lower() == "true":
                    # Set the value to True
                    value = True
                elif value.lower() == "false":
                    # Set the value to False
                    value = False

                elif value.isdigit():
                    # Set the value to an integer
                    value = int(value)

                elif value.lower() == "none":
                    # Set the value to None
                    value = None

                # Check if the section is not in the config
                else:
                    value = str(value)

                # Check if the section is not in the config
                if section.lower() not in config:
                    # Create a new section
                    config[section.lower()] = {}

                # Set the value
                config[section.lower()][option.lower()] = value

        # Return the config
        return config
