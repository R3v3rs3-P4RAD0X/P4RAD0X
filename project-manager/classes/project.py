# Imports
import datetime
import json
import os


class Project:
    name: str
    language: str
    description: str
    working_directory: str

    creation_date: datetime.datetime
    last_modified_date: datetime.datetime
    last_modified_file: str

    files: list[str]

    def __init__(self, projects_directory: str) -> None:
        self.name = ""
        self.language = ""
        self.description = ""
        self.projects_directory = projects_directory

        self.creation_date = datetime.datetime.now()
        self.last_modified_date = datetime.datetime.now()
        self.last_modified_file = ""

        self.files = []

    def new(self, name: str, language: str, description: str) -> None:
        self.name = name
        self.language = language
        self.description = description
        self.working_directory = self.create_working_directory

        self.creation_date = datetime.datetime.now()
        self.last_modified_date = datetime.datetime.now()

        self.files = []

    def to_json(self, indent=4) -> str:
        # Create the dictionary.
        data = {}

        # Add the name, language, and description.
        data["name"] = self.safe_name()
        data["language"] = self.language
        data["description"] = self.description

        # Add the creation date and last modified date.
        data["creation_date"] = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        data["last_modified_date"] = self.last_modified_date.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Add the project directory.
        data["working_directory"] = self.working_directory()

        # Add the files.
        data["files"] = self.get_files()

        # Return the JSON.
        return json.dumps(data, indent=indent)

    def safe_name(self) -> str:
        return self.name.replace(" ", "-").lower()

    def get_files(self) -> list[str]:
        # Walk the project directory and return all the files
        # in the project.
        return []

    def create_working_directory(self) -> str:
        # Create the working directory.
        return os.path.join(self.projects_directory, self.language, self.safe_name())


# Testing
if __name__ == "__main__":
    project = Project()
    project.new(
        name="Test Project",
        language="Python",
        description="A test project.",
    )
    print(project.to_json())
