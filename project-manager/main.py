# Imports
from errors import CreationError
from creator import Creator, LANGUAGES
from tracker import Tracker
from functions import ask, read_env

# Create the main function
def main():
    # Read the environment variables
    env = read_env()

    # Create a creator object
    creator = Creator()

    # Create a tracker object
    tracker = Tracker()

    # Ask for the project name
    name = ask("What is the name of the project?", check=lambda x: len(x) > 0 and len(x) < 50)

    # Ask for the project description
    description = ask("What is the description of the project?", check=lambda x: len(x) > 0 and len(x) < 100)

    # Check if description has a . at the end
    if description[-1] != ".":
        # Add a . at the end
        description += "."

    # Ask for the project language
    language = LANGUAGES[ask("What is the language of the project?", options=list(LANGUAGES.keys()))]

    # Create the project data
    creator.set_name(name)
    creator.set_description(description)
    creator.set_language(language)
    creator.set_path(env["PROJECTS_DIRECTORY"])

    # Set the project of the tracker
    tracker.set_project(creator)

    # Create the project
    try:
        creator.create()
        tracker.track()

    except CreationError as e:
        print(e)

    except Exception as e:
        print(f"An error occurred: {e}")

# Check if the file is being run directly
if __name__ == '__main__':
    # Run the main function
    main()