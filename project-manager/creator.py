import os
from errors import CreationError
from functions import call

LANGUAGES = {
    "python": "python",
    "py": "python",
    "rust": "rust",
    "rs": "rust",
    "ruby": "ruby",
    "rb": "ruby",
    "go": "go",
    "golang": "go",
    "bash": "bash",
    "sh": "bash",
    "cpp": "cpp",
    "c++": "cpp",
    "web": "web",
}

class Creator:
    """
    The Creator class is responsible for creating new projects based on the provided parameters.
    """

    def __init__(self):
        self.name = None
        self.description = None
        self.language = None
        self.path = None

    def set_name(self, name: str):
        """
        Sets the name of the object.

        Parameters:
        name (str): The name to be set.

        Returns:
        self: The current object.
        """
        self.name = name
        return self

    def set_description(self, description: str):
        """
        Sets the description of the project.

        Parameters:
        - description (str): The description of the project.

        Returns:
        - self: The current instance of the Creator class.
        """
        self.description = description
        return self
    
    def set_language(self, language):
        """
        Sets the language of the project.

        Parameters:
        - language (str): The language of the project.

        Returns:
        - self: The current instance of the Creator class.
        """
        self.language = language
        return self
    
    def set_path(self, path):
        """
        Sets the path of the project.

        Parameters:
        - path (str): The path of the project.

        Returns:
        - self: The current instance of the Creator class.
        """
        # Construct the path
        self.path = os.path.join(path, self.language, self.name)
        return self
    
    def create(self) -> None:
        """
        Create a new project based on the provided parameters.
        """
        # Check if the project already exists
        if os.path.exists(self.path):
            # Raise an error
            raise CreationError(f"Project with name '{self.name}' already exists")
        
        # Check the language provided
        if self.language not in LANGUAGES:
            # Raise an error
            raise CreationError(f"Invalid language: {self.language}")

        # Check the language
        match self.language:
            case "rust":
                # Create the project and pipe into /dev/null
                call(f"cargo new {self.name} --quiet", devnull=True)

            case _:
                # Create the project
                os.system(f"mkdir {self.path}")

        # Create the README
        with open(os.path.join(self.path, "README.md"), "w") as f:
            f.write(f"# {self.name}\n\n{self.description}")

        # Create the .env
        with open(os.path.join(self.path, ".env"), "w") as f:
            f.write("")

        # Create language specific files
        match self.language:
            case "python":
                # Create the main file
                with open(os.path.join(self.path, "main.py"), "w") as f:
                    f.write("# Imports\n\n\n# Create the main function\n\ndef main():\n    pass\n\n\n# Check if the file is being run directly\nif __name__ == '__main__':\n    # Run the main function\n    main()")

                # Create the requirements.txt
                with open(os.path.join(self.path, "requirements.txt"), "w") as f:
                    f.write("")
            
            case "ruby":
                # Create the main file
                with open(os.path.join(self.path, "main.rb"), "w") as f:
                    f.write("# Create the main function\n\ndef main\n    # Code\nend\n\n\n# Check if the file is being run directly\nif __FILE__ == $0\n    # Run the main function\n    main\nend")
            
            case "go":
                # Create the main file
                with open(os.path.join(self.path, "main.go"), "w") as f:
                    f.write("package main\n\n\nfunc main() {\n    // Code\n}")

                # Create the go.mod
                with open(os.path.join(self.path, "go.mod"), "w") as f:
                    f.write("module main")

            case "bash":
                # Create the main file
                with open(os.path.join(self.path, "main.sh"), "w") as f:
                    f.write("# Create the main function\n\nfunction main() {\n    # Code\n}\n\n\n# Check if the file is being run directly\nif [[ ${BASH_SOURCE[0]} == ${0} ]]; then\n    # Run the main function\n    main\nfi")

                # Chmod the file
                os.system(f"chmod +x {os.path.join(self.path, 'main.sh')}")

            case "cpp":
                # Create the main file
                with open(os.path.join(self.path, "main.cpp"), "w") as f:
                    f.write("#include <iostream>\n\n\nint main() {\n    // Code\n    return 0;\n}")

                # Create the Makefile
                with open(os.path.join(self.path, "Makefile"), "w") as f:
                    f.write("all:\n\tg++ main.cpp -o main\n\nrun:\n\t./main")

            case "web":
                # Create the index.html
                with open(os.path.join(self.path, "index.html"), "w") as f:
                    f.write("<!DOCTYPE html>\n<html>\n    <head>\n        <title></title>\n    </head>\n    <body>\n        \n    </body>\n</html>")

                # Create the style.css
                with open(os.path.join(self.path, "style.css"), "w") as f:
                    f.write("")

                # Create the main.js
                with open(os.path.join(self.path, "main.js"), "w") as f:
                    f.write("")

            case _:
                pass

        # Print a success message
        print(f"Successfully created project '{self.name}'")
        print(f"Path: {self.path}")
