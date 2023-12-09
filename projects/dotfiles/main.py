"""
This script handles the automatic linking and backing up of dotfiles.
"""

import dataclasses
import json

# Imports #
import os
import shutil

# Constants #
HOME = os.getenv("HOME")
CONFIG = os.path.join(HOME, ".config")
BACKUP = os.path.join(CONFIG, "BACKUP")
DOTFILES = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "storage", "dotfiles")
)


# Dataclass to represent a dotfile
@dataclasses.dataclass
class Dotfile:
    name: str
    source: os.PathLike
    destination: os.PathLike
    subdirectories: list[str] = dataclasses.field(default_factory=list)


# Main Class
class Main:
    def __init__(self):
        # Create any directories that might not exist
        self.ensure_directories()
        self.dotfiles = self.get_dotfiles()
        self.check_dotfiles()
        self.link_dotfiles()

    def ensure_directories(self):
        # Create the config directory if it doesn't exist
        if not os.path.exists(CONFIG):
            os.mkdir(CONFIG)

            # Print an alert that the directory was created
            print("Created config directory")
            print(CONFIG, end="\n\n")

        # Create the backup directory if it doesn't exist
        if not os.path.exists(BACKUP):
            os.mkdir(BACKUP)

            # Print an alert that the directory was created
            print("Created backup directory")
            print(BACKUP)

    def get_dotfiles(self) -> list[Dotfile]:
        """
        Method that will return a list of Dotfiles including all the dotfiles
        """
        # Create a dotfiles list
        dotfiles = []

        # Iterate over the dotfiles directory
        for root, _, files in os.walk(DOTFILES):
            # Iterate over the files
            for file in files:
                # Check if there is a subdirectory
                subdirectories = [
                    sd
                    for sd in (
                        root.replace(DOTFILES, "").replace(file, "").split(os.sep)
                    )
                    if len(sd) > 0
                ]

                # Create a new dotfile
                dotfiles.append(
                    Dotfile(
                        name=file,
                        source=os.path.join(root, file),
                        destination=os.path.join(
                            CONFIG,
                            *subdirectories if len(subdirectories) > 0 else "",
                            file,
                        ),
                        subdirectories=subdirectories or None,
                    )
                )

        # Return the dotfiles
        return dotfiles

    def check_dotfiles(self):
        """
        A method that will check the dotfiles.
        If the dotfiles destination exists, it will be backed up.
        """

        # Iterate over the dotfiles
        for dotfile in self.dotfiles:
            # Check if the destination exists
            if os.path.exists(dotfile.destination):
                # Check if the dotfile destination is a link
                if os.path.islink(dotfile.destination):
                    # Get the source of the link
                    link_source = os.readlink(dotfile.destination)

                    # Write into the BACKUP/links.txt file
                    with open(os.path.join(BACKUP, "links.txt"), "a") as f:
                        f.write(f"{dotfile.destination} -> {link_source}\n")

                    # Remove the link
                    os.remove(dotfile.destination)

                    # Print an alert that the link was removed
                    print(f"Removed link: {dotfile.destination}")

                # Check if the dotfile destination is a file
                elif os.path.isfile(dotfile.destination):
                    # Check any subdirectories
                    if dotfile.subdirectories:
                        # Create the subdirectories
                        for subdirectory in dotfile.subdirectories:
                            # Create the subdirectory
                            os.makedirs(os.path.join(HOME, subdirectory), exist_ok=True)

                            # Print an alert that the subdirectory was created
                            print(f"Created subdirectory: {subdirectory}")

                    # Move the file to the backup directory
                    shutil.move(
                        dotfile.destination,
                        os.path.join(BACKUP, dotfile.name),
                    )

                    # Print an alert that the file was moved
                    print(f"Moved file: {dotfile.destination}")

                # Check if the dotfile destination is a directory
                elif os.path.isdir(dotfile.destination):
                    # Move the directory to the backup directory
                    shutil.move(
                        dotfile.destination,
                        os.path.join(BACKUP, dotfile.name),
                    )

                    # Print an alert that the directory was moved
                    print(f"Moved directory: {dotfile.destination}")

            # Check if the source exists
            if not os.path.exists(dotfile.source):
                # Print an alert that the source doesn't exist
                print(f"Source doesn't exist: {dotfile.source}")

    def link_dotfiles(self):
        """
        A method that will link the dotfiles.
        """

        # Iterate over the dotfiles
        for dotfile in self.dotfiles:
            # Check if the destination exists
            if not os.path.exists(dotfile.destination):
                # Check any subdirectories
                if dotfile.subdirectories:
                    # Create the subdirectories
                    for subdirectory in dotfile.subdirectories:
                        # Create the subdirectory
                        os.makedirs(os.path.join(CONFIG, subdirectory), exist_ok=True)

                        # Print an alert that the subdirectory was created
                        print(f"Created subdirectory: {subdirectory}")

                # Create the link
                os.symlink(dotfile.source, dotfile.destination)

                # Print an alert that the link was created
                print(f"Created link: {dotfile.destination}")


# If the script is ran directly
if __name__ == "__main__":
    # Create a new instance of the main class
    main = Main()
