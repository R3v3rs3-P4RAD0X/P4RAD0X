# Imports
from creator import Creator
from tracker import Tracker


# Functions
def read_env(file: str) -> dict[str, str]:
    # Create the dictionary.
    data = {}

    # Open the file.
    with open(file, "r") as f:
        # Read the lines.
        lines = f.readlines()

        # Loop through the lines.
        for line in lines:
            # Check if the line is a comment.
            if line.startswith("#"):
                # Skip the line.
                continue

            # Split the line.
            key, value = line.split("=")

            # Add the key and value to the dictionary.
            data[key] = value.strip()

    # Return the dictionary.
    return data


# Main
def main():
    # Read the environment variables.
    env = read_env(".env")

    # Create the creator and tracker.
    creator = Creator()
    tracker = Tracker()

    project = creator.new(env["PROJECTS_DIRECTORY"])

    print(project.to_json())


# Run the main function.
if __name__ == "__main__":
    main()
