"""
The main script for the project manager.
"""

# Imports
import os

# Import the creation module
from creation import Creator

# Import the helper functions
from utils import helper


# Create a main function
def main():
    # Load the env file
    env = helper.load_env(".env")

    # Create a creator object
    creator = Creator(env["PROJECTS_DIRECTORY"])

    # Run the creator commands
    data = creator.create()

    # Clear the screen
    os.system("clear" if os.name == "posix" else "cls")

    # Call the tracker function
    os.system(
        " ".join(
            [
                "python",
                "tracker/tracker.py",
                "--name",
                data["name"],
                "--lang",
                data["lang"],
                "--path",
                data["path"],
                "--create",
            ]
        )
    )

    # Print the new project from the tracker
    print("New project:")
    os.system(
        " ".join(
            ["python", "tracker/tracker.py", "-lsp", f'{data["lang"]}.{data["name"]}']
        )
    )


# If ran directly
if __name__ == "__main__":
    # Check if .venv is activated
    if not helper.is_venv():
        print("Please activate your virtual environment.")
        exit(1)
        
    # Run the main function
    main()