"""
This file will have a bunch of utility functions that will be used in the main file.
"""

# Imports
import os
import re

# Constants
ENV_REGEX = r"([A-Z_]+)=(.*)"


# A function that counts the total number of lines in a file.
def count_lines(file):
    i = 0
    with open(file, "r") as f:
        for i, l in enumerate(f):
            if l == "\n":
                i = i - 1
    return i + 1


# A function that counts the total number of words in a file.
def count_words(file):
    i = 0
    with open(file, "r") as f:
        for i, l in enumerate(f.read().split()):
            pass
    return i + 1


# A function that gets the last modified date of a file.
def last_modified(file):
    return os.path.getmtime(file)


# A function that gets the size of a file.
def size(file):
    return os.path.getsize(file)


# A function that gets the latest modified file in a directory
def latest_modified(directory):
    return (
        max(
            [os.path.join(directory, f) for f in os.listdir(directory)],
            key=os.path.getmtime,
        ),
    )[0]


# A function that prints a table
def tabulate(columns: list[str], rows: list[str]) -> None:
    # Get the maximum length of each column
    max_lengths = [len(column) for column in columns]

    # Get the maximum length of each row
    for row in rows:
        for i, column in enumerate(row):
            if len(column) > max_lengths[i]:
                max_lengths[i] = len(column)

    # Print the table with headers
    print(
        " | ".join([column.ljust(max_lengths[i]) for i, column in enumerate(columns)])
    )
    print("-+-".join(["-" * max_length for max_length in max_lengths]))
    for row in rows:
        print(
            " | ".join([column.ljust(max_lengths[i]) for i, column in enumerate(row)])
        )


# A function that loads a .env file
def load_env(file: str) -> dict[str, str]:
    # Create a dictionary to store the env variables
    env = {}

    # OPEN THE FILE
    with open(file, "r") as f:
        # Get the lines
        lines = f.readlines()

        # Iterate over the lines
        for idx, line in enumerate(lines):
            # Check if the line is empty or a new line
            if not line or line == "\n":
                continue

            # Check if the line is a comment
            if line.startswith("#"):
                continue

            # Check if the line has a valid format key=value
            if not re.match(ENV_REGEX, line):
                raise Exception(f"Invalid format for line: {idx + 1} in file: {file}")

            # Get the key and value
            key, value = line.split("=")

            # Check if the key is already in the env
            if key in env:
                raise Exception(f"Duplicate key: {key} in file: {file}")

            # Check if the value is empty
            if not value.strip():
                raise Exception(f"Empty value for key: {key} in file: {file}")

            # Check if the line has " or '
            if '"' in value or "'" in value:
                raise Exception(
                    f"Invalid character in value for key: {key} in file: {file}"
                )

            # Add the key and value to the env
            env[key] = value.strip()

    # Return the env
    return env

# A function to determine if the virtual environment is activated
def is_venv() -> bool:
    return os.getenv("VIRTUAL_ENV") is not None