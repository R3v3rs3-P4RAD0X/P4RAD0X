"""
This class will have all the functions for creating a new project.
"""

# Imports
import os
from typing import Any


# A class that creates a new project
class Creator:
    LANGUAGES = {
        "python": "python",
        "py": "python",
        "javascript": "javascript",
        "js": "javascript",
        "ruby": "ruby",
        "rb": "ruby",
        "cpp": "cpp",
        "c++": "cpp",
        "rust": "rust",
        "rs": "rust",
        "go": "go",
        "golang": "go",
        "bash": "bash",
        "sh": "bash",
        "html": "web",
        "css": "web",
        "web": "web",
    }

    def __init__(self, projects_path: str):
        self.name = ""
        self.lang = ""
        self.desc = ""

        self.projects_path = projects_path

    # A function to get the name for the project
    def get_name(self) -> str:
        name = input("Enter the name of the project: ")
        self.name = name

        return name

    def get_lang(self) -> str:
        # Create a list of all the languages
        languages = list(set(self.LANGUAGES.values()))

        # Print the languages
        print("Languages:")
        for lang in languages:
            print(f"\t{lang}")

        lang = None

        while lang not in languages:
            lang = input("Enter the language: ")

            if lang not in languages:
                print("Invalid language.")
                continue

        self.lang = lang

        return lang

    def get_desc(self) -> str:
        desc = input("Enter the description: ")
        self.desc = desc

        return desc

    def create(self) -> dict:
        # Get the name
        self.get_name()

        # Get the language
        self.get_lang()

        # Get the description
        self.get_desc()

        # Create the path
        return self.create_project()

    def create_project(self):
        # In the following format: projects_path/lang/name
        path = os.path.join(self.projects_path, self.lang, self.name)

        # If the language is rust, use cargo to create the new project
        if self.lang == "rust":
            os.system(f"cargo new {path}")

        else:
            # Create the project directory
            os.makedirs(path)

        # Create the README.md file
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(f"# {self.name}\n\n{self.desc}")

        # Create the .gitignore file
        with open(os.path.join(path, ".gitignore"), "w") as f:
            f.write("")

        match self.lang.lower():
            case "python":
                # Create the main.py file
                with open(os.path.join(path, "main.py"), "w") as f:
                    f.write("")

                # Initialise the virtual environment
                os.system(f"python3 -m venv {os.path.join(path, '.venv')}")

                # Create an empty requirements.txt file
                with open(os.path.join(path, "requirements.txt"), "w") as f:
                    f.write("")

            case "javascript":
                # Create the index.js file
                with open(os.path.join(path, "index.js"), "w") as f:
                    f.write("")

            case "ruby":
                # Create the main.rb file
                with open(os.path.join(path, "main.rb"), "w") as f:
                    f.write("")

            case "cpp":
                # Create the main.cpp file
                with open(os.path.join(path, "main.cpp"), "w") as f:
                    f.write("")

                # Create a makefile
                with open(os.path.join(path, "makefile"), "w") as f:
                    # Add a basic makefile
                    f.write("CC=g++\n\n")

                    f.write("all:\n")
                    f.write("\t$(CC) main.cpp -o main\n\n")

                    f.write("clean:\n")
                    f.write("\trm main\n")

            case "go":
                # Create the main.go file
                with open(os.path.join(path, "main.go"), "w") as f:
                    f.write("")

            case "bash":
                # Create the main.sh file
                with open(os.path.join(path, "main.sh"), "w") as f:
                    f.write("#!/bin/bash\n")

            case "web":
                # Create the index.html file
                with open(os.path.join(path, "index.html"), "w") as f:
                    f.write("")

                # Create the static directory with two sub directories js and css
                os.makedirs(os.path.join(path, "static", "js"))
                os.makedirs(os.path.join(path, "static", "css"))

                # Create the main.js file
                with open(os.path.join(path, "static", "js", "main.js"), "w") as f:
                    f.write("")

                # Create the main.css file
                with open(os.path.join(path, "static", "css", "main.css"), "w") as f:
                    f.write("")

            case _:
                pass

        # Return a dictionary with the project information
        return {
            "name": self.name,
            "lang": self.lang,
            "desc": self.desc,
            "path": path,
        }
