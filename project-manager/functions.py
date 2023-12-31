import time
import re
import subprocess
import os

# CONSTANTS
# The regex pattern for checking if key=value is valid
KEY_VALUE_REGEX = re.compile(r"^[a-zA-Z0-9_]+=.*$")
# A list of directories to avoid
AVOID_DIRECTORIES = [
    "database", 
    "target", 
    "build", 
    "venv", 
    ".venv", 
    "__pycache__", 
    ".git",
    ".idea",
    ".vscode",
]

def ask(question: str, options: list[str] = None, check: callable = None, rtype: type = str):
    """
    Prompts the user with a question and returns their input.

    Args:
        question (str): The question to ask the user.
        options (list[str], optional): The list of valid options. Defaults to None.
        check (callable, optional): A function to check the validity of the input. Defaults to None.
        rtype (type, optional): The expected return type of the input. Defaults to str.

    Returns:
        Any: The user's input, converted to the specified return type if provided.
    """
    # Function implementation...
def ask(question: str, options: list[str] = None, check: callable = None, rtype: type = str):
    # Print the question
    print(f"{question}:")

    # Check if options are provided
    if options and len(options) > 0:
        # Print the options
        for i, option in enumerate(options):
            print(f"  - {option}")

    # Create a loop
    while True:
        # Get the input
        inp = input("> ")

        # Check if options are provided
        if options and len(options) > 0:
            # Check if the input is valid
            if inp not in options:
                # Print an error
                print(f"Invalid option: {inp}")
                time.sleep(1)

                # Continue the loop
                continue

        # Check if a check function is provided
        if check and callable(check):
            # Check if the input is valid
            if not check(inp):
                # Print an error
                print(f"Invalid input: {inp}")
                time.sleep(1)

                # Continue the loop
                continue
        
        # Check if a return type is provided
        if rtype:
            # Convert the input
            try:
                inp = rtype(inp)
            except ValueError:
                # Print an error
                print(f"Invalid input: {inp}")
                time.sleep(1)

                # Continue the loop
                continue

        # Return the input
        return inp
    

def read_env() -> dict:
    """
    Reads the .env file and returns a dictionary of the environment variables.

    Returns:
        dict: The environment variables.
    """
    try:
        with open(".env", "r") as f:
            # Get the lines
            lines = f.readlines()

            # Create a dictionary
            env = {}

            # Loop through the lines
            for line in lines:
                # Strip the line
                line = line.strip()

                # Check if the line is empty
                if len(line) == 0:
                    # Continue the loop
                    continue

                # Check if the line is a comment
                if line.startswith("#"):
                    # Continue the loop
                    continue

                # Check if the line is valid
                if KEY_VALUE_REGEX.match(line):
                    # Split the line
                    key, value = line.split("=")

                    # Add the key and value to the dictionary
                    env[key] = value

            # Return the dictionary
            return env

    except FileNotFoundError:
        # Print an error
        print("The .env file is missing.")
        time.sleep(1)
        exit(1)

    except Exception as e:
        # Print an error
        print(f"An error occurred: {e}")
        time.sleep(1)
        exit(1)

def call(command: str, args: list[str] = None, devnull: bool = True) -> dict:
    """
    Calls a command and returns the output.

    Args:
        command (str): The command to call.
        args (list[str], optional): The arguments to pass to the command. Defaults to None.

    Returns:
        dict: The output of the command.
    """
    # Create the command
    cmd = [command]

    # Check if arguments are provided
    if args and len(args) > 0:
        # Add the arguments to the command
        cmd.extend(args)

    # Create a variable to store the pipe
    pipe = subprocess.PIPE if not devnull else subprocess.DEVNULL

    # Run the command
    process = subprocess.run(cmd, stdout=pipe, stderr=pipe, shell=True)

    # Return the output
    return {
        "stdout": process.stdout.decode("utf-8") if process.stdout else "",
        "stderr": process.stderr.decode("utf-8") if process.stderr else ""
    }

def walk(dir: str, files: list[str] = None) -> list[str]:
    """
    Returns a list of files in the specified directory.

    Args:
    - dir (str): The directory to get the files from.

    Returns:
    - list[str]: The list of files in the specified directory.
    """
    # Create a list to store the files
    if not files or len(files) == 0:
        files = []

    # Check if files is a list
    if not isinstance(files, list):
        # Raise an error
        raise TypeError("files must be a list")

    # Loop through the files
    for file in os.listdir(dir):
        # Get the path
        path = os.path.join(dir, file)

        # Check if the path is a directory
        if os.path.isdir(path):
            # Check if the directory should be avoided
            if file in AVOID_DIRECTORIES:
                # Continue the loop
                continue

            # Get the files in the directory
            walk(path, files)

        # Check if the path is a file
        if os.path.isfile(path):
            # Add the file to the list
            files.append(path)

    # Return the list
    return files