# Imports
import os
import subprocess

from classes import Project
from error import CreationError


def setup(project: Project) -> None:
    # Get the safe name
    safe_name = project.get_safe_name()

    # Check if the project is a python project.
    if project.language != "python":
        # Raise an error.
        raise CreationError("The project is not a python project.")

    # Check if the project directory exists.
    if os.path.exists(project.working_directory):
        # Raise an error.
        raise CreationError("The project directory already exists.")

    # Create the project directory.
    os.mkdir(project.working_directory)

    # Create the main.py file
    with open(f"{project.working_directory}/main.py", "w") as f:
        # Write the file.
        f.write("# Imports\n")
        f.write("\n")
        f.write("\n")
        f.write("# Functions\n")
        f.write("def main():\n")
        f.write("    pass\n")
        f.write("\n")
        f.write("\n")
        f.write("# Run the main function.\n")
        f.write('if __name__ == "__main__":\n')
        f.write("    main()\n")

    # Create the .gitignore file
    with open(f"{project.working_directory}/.gitignore", "w") as f:
        # Write the file.
        f.write(".env\n")
        f.write("__pycache__/\n")
        f.write("venv/\n")

    # Create the README.md file
    with open(f"{project.working_directory}/README.md", "w") as f:
        # Write the file.
        f.write(f"# {project.name}\n")
        f.write("\n")
        f.write(f"{project.description}\n")

    # Create the .env file
    with open(f"{project.working_directory}/.env", "w") as f:
        # Write the file.
        f.write(f"PROJECT_NAME={project.name}\n")
        f.write(f"PROJECT_DESCRIPTION={project.description}\n")
        f.write(f"PROJECT_LANGUAGE={project.language}\n")

    # Create the requirements.txt file
    with open(f"{project.working_directory}/requirements.txt", "w") as f:
        # Write the file.
        f.write("")

    # Create the venv
    subprocess.run(["python", "-m", "venv", f"{project.working_directory}/venv"])

    # Return a success message.
    return f"Successfully created the project {project.name}."
