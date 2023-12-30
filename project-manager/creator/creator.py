# Imports
import setup
from classes import CreationError, Project

# Constants #
# --------- #
LANGUAGES = {
    "python": "py",
    "rust": "rs",
    "cpp": "cpp",
    "go": "go",
    "ruby": "rb",
    "nodejs": "js",
    "web": "web",
}


# A class to create a new project.
class Creator:
    def new(self, projects_directory: str) -> Project:
        # Ask the user some questions.
        name = self.ask(
            "What is the name of the project? ",
            check=lambda name: len(name) > 0 and len(name) < 50,
        )

        language = self.ask(
            "What is the language of the project? ",
            valid_options=[*LANGUAGES.values(), *LANGUAGES.keys()],
        )

        description = self.ask(
            "What is the description of the project? ",
            check=lambda description: len(description) > 0,
        )

        # Convert the language to the key if it is the value.
        if language in LANGUAGES.values():
            language = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(language)]

        # Create the project.
        project = Project(projects_directory)
        project.new(
            name,
            language,
            description,
        )

        # Match the language
        match language:
            case "python":
                setup.python_setup(project)

            case _:
                raise CreationError("The language is not supported.")

        # Return the project.
        return project

    def ask(
        self, question: str, valid_options: list[str] = None, check: callable = None
    ) -> str:
        # Check if there is valid_options
        if valid_options:
            # Print the options
            print("Options:")
            for option in valid_options:
                print(f" - {option}")

        # Ask the question.
        answer = input(question)

        # Check if the answer is valid.
        if valid_options and answer not in valid_options:
            # Print an error message.
            print("Invalid answer.")

            # Ask the question again.
            answer = self.ask(question, valid_options)

        # Check if the answer is valid.
        if check is not None:
            # Check the answer.
            if check(answer) is False:
                # Print an error message.
                print("Invalid answer.")

                # Ask the question again.
                answer = self.ask(question, valid_options, check)

        # Return the answer.
        return answer
