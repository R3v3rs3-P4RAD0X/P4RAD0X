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
        
    @staticmethod
    def readConfig():
        """
        Reads the config file and returns the contents.

        :return: The contents of the config file.
        """
        # Get the path to the config file
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config"))

        # Get all the lines with two fields, separated by an equals sign
        # Using awk -F ' = ' '/^[^;]/ { print $1"="$2 }' your_config_file
        fields = System.call_output(f"awk -F ' = ' '/^[^;]/ {{ print $1\"=\"$2 }}' {path}").split("\n")

        # Set the config dictionary
        config = {}

        # Loop through the fields
        for field in fields:
            # Check if the field is not empty
            if field:
                # Get the value for the field
                key, val = field.split("=")

                # Set the value in the config dictionary
                config[key] = val

        # Return the config dictionary
        return config