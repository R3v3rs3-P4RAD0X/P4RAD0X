"""
Welcome to the tracker file.

The Tracker is independent of the main file.
To call it from the main file, use the following code:

os.system("python tracker/tracker.py - [args]")
"""

# Imports
import argparse
import json
import os
import shutil
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils import helper


class Tracker:
    def __init__(self):
        self.storage = "/P4RAD0X/project-manager/tracker/storage.json"

    def open_storage(self) -> dict:
        # Check if the self.storage file exists
        if not os.path.exists(self.storage):
            # Create the file
            with open(self.storage, "w") as f:
                json.dump({}, f)

        # Open the file
        with open(self.storage, "r") as f:
            return json.load(f)

    def save_storage(self, data: dict) -> None:
        # Save the data
        with open(self.storage, "w") as f:
            json.dump(data, f, indent=4)

    def create_project(self, path: str, name: str, language: str) -> None:
        # Check if the project exists at the path
        if not os.path.exists(path):
            return

        # Get the storage
        storage = self.open_storage()

        # Construct the name for the project in the format lang.name
        project_name = f"{language}.{name}"

        # Check if the project already exists
        if project_name in storage:
            raise Exception("Project already exists.")

        # Create the project
        storage[project_name] = {
            "path": path,
            "name": name,
            "language": language,
            "last_edited": helper.latest_modified(path),
            "files": {},
        }

        # Populate the files
        storage[project_name] = self.populate_files(storage[project_name])

        # Save the storage
        self.save_storage(storage)

    def populate_files(self, project: dict) -> dict:
        # Get the files in the project
        files = os.listdir(project["path"])

        # Populate the files
        for file in files:
            # Get the path to the file
            path = os.path.join(project["path"], file)

            # Check if the file is a directory
            if os.path.isdir(path):
                # Skip the directory
                continue

            # Get the file's stats
            stats = {
                "lines": helper.count_lines(path),
                "words": helper.count_words(path),
                "last_modified": helper.last_modified(path),
                "size": helper.size(path),
            }

            # Add the file to the project
            project["files"][file] = stats

        return project

    def sync(self) -> None:
        # Get the storage
        storage = self.open_storage()

        # Loop through the projects
        for project in storage:
            # Get the project
            project = storage[project]

            # Print Syncing message | Language: Name
            print(f"Syncing project: {project['language']}.{project['name']}")

            # Check if the project exists
            if not os.path.exists(project["path"]):
                # Delete the project
                del storage[project]

                # Continue to the next project
                continue

            # Check if the project has been modified
            if project["last_edited"] != helper.latest_modified(project["path"]):
                # Update the project
                project["last_edited"] = helper.latest_modified(project["path"])
                project = self.populate_files(project)

            # Save the storage
            self.save_storage(storage)

    def delete(self, project_name: str) -> None:
        # Get the storage
        storage = self.open_storage()

        # Check if the project exists
        if project_name not in storage:
            raise Exception("The project does not exist.")

        # Get the project from the storage
        project = storage[project_name]

        # Get the path
        path = project["path"]

        # Try delete the project
        try:
            # Delete from storage
            del storage[project_name]

            # Delete the project
            shutil.rmtree(path)
        # If an error occurs
        except Exception as e:
            print("Project already deleted.")
            print(e)

        # Save the storage
        self.save_storage(storage)


# If ran directly
if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(
        description="A file tracker that tracks files and directories."
    )

    # Add the arguments #
    # Arg 1: The project path
    parser.add_argument(
        "-p",
        "--path",
        metavar="path",
        type=str,
        help="The path to the project.",
    )

    # Arg 2: The name of the project
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        help="The name of the project.",
    )

    # Arg 3: The path to the project's language
    parser.add_argument(
        "-l",
        "--language",
        metavar="language",
        type=str,
        help="The language of the project.",
    )

    # Arg 4: Sync the projects
    parser.add_argument("-s", "--sync", action="store_true", help="Sync the projects.")

    # Arg 5: Create a new project
    parser.add_argument(
        "-c", "--create", action="store_true", help="Create a new project."
    )

    # Arg 6: List the projects
    parser.add_argument("-ls", "--list", action="store_true", help="List the projects.")

    # Arg 7: List a specific project
    parser.add_argument(
        "-lsp",
        "--list_specific",
        metavar="project",
        type=str,
        help="List a specific project. Use the format lang.name",
    )

    # Arg 8: Delete a project
    parser.add_argument(
        "-d",
        "--delete",
        metavar="project",
        type=str,
        help="Delete a project.",
    )

    # Arg 9: API
    parser.add_argument(
        "-a",
        "--api",
        action="store_true",
        help="Returns data in JSON format.",
    )

    # Check if no arguments were passed
    if len(sys.argv) == 1:
        # Print the help message
        parser.print_help()

        # Exit the program
        sys.exit(1)

    # Create the tracker
    tracker = Tracker()

    # Parse the arguments
    args = parser.parse_args()

    # Check if args.path is a directory
    if args.path and not os.path.isdir(args.path):
        raise Exception("The path must be a directory.")

    # Check if args.name is a string
    if args.name and (not isinstance(args.name, str) or len(args.name) == 0):
        raise Exception("The name must be a string.")

    # Check if args.language is a string
    if args.language and (
        not isinstance(args.language, str) or len(args.language) == 0
    ):
        raise Exception("The language must be a string.")

    # Check if args.sync is set to True
    if args.sync:
        # Sync the projects
        tracker.sync()

    # Check if args.create is set to True
    if args.create:
        # Try to create the project
        try:
            # Create the project
            tracker.create_project(args.path, args.name, args.language)

            # Print a success message
            print("Successfully created the project.")

        # If an error occurs
        except Exception as e:
            print(e)

    # Check if args.list is set to True
    if args.list:
        # Get the storage
        storage = tracker.open_storage()

        # Check if there are no projects
        if len(storage) == 0:
            # Print a message
            print("There are no projects.")

            # Exit the program
            sys.exit(1)

        # Create the columns
        columns = ["Index", "Language", "Name", "Path", "Tracker Name"]

        # Create the rows
        rows = []

        # Sort the storage by the language then the name
        storage = dict(sorted(storage.items(), key=lambda x: x[1]["language"]))

        # Loop through the projects
        for i, project in enumerate(storage):
            # Get the project
            project = storage[project]

            # Add the row
            rows.append(
                [
                    str(i + 1).rjust(3, "0").rjust(5, " "),
                    project["language"].title(),
                    project["name"],
                    project["path"],
                    f"{project['language']}.{project['name']}",
                ]
            )

        # Print the table
        helper.tabulate(columns, rows)

    # Check if args.list_specific is set to True
    if args.list_specific and (args.list_specific != "" or len(args.list_specific) > 0):
        # Get the storage
        storage = tracker.open_storage()

        # Check if the project exists
        if args.list_specific not in storage:
            # Print a message
            print("The project does not exist.")

            # Exit the program
            sys.exit(1)

        # Get the project
        project = storage[args.list_specific]

        # Create the columns
        columns = ["Index", "Key", "Value"]

        # Create the rows
        rows = []

        # Loop through the project
        for i, file in enumerate(project.keys()):
            # Check if the file is files
            if file == "files":
                # Skip the file
                continue

            # Add the row
            rows.append(
                [
                    str(i + 1).rjust(3, "0").rjust(5, " "),
                    file,
                    project[file],
                ]
            )

        # Print the table
        helper.tabulate(columns, rows)

    # Check if args.delete is set to True
    if args.delete and (args.delete != "" or len(args.delete) > 0):
        # Get the storage
        storage = tracker.open_storage()

        # Check if the project exists
        if args.delete not in storage:
            # Print a message
            print("The project does not exist.")

            # Exit the program
            sys.exit(1)

        # Delete the project
        del storage[args.delete]

        # Call tracker.delete
        tracker.delete(args.delete)

        # Save the storage
        tracker.save_storage(storage)

        # Print a success message
        print("Successfully deleted the project.")

    # Check if args.api is set to True
    if args.api:
        # Get the storage
        storage = tracker.open_storage()

        # Print the storage
        print(json.dumps(storage, indent=4))