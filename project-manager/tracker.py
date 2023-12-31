from creator import Creator
import os
import json
from functions import walk

class Tracker:
    def __init__(self):
        self.project: Creator = None

    def set_project(self, project: Creator) -> 'Tracker':
        """
        Sets the project of the tracker.

        Parameters:
        - project (Creator): The project to be set.

        Returns:
        - self: The current instance of the Tracker class.
        """
        self.project = project
        return self
    
    def track(self) -> None:
        """
        Tracks the project.

        Returns:
        - None
        """
        # Create the storage directory
        sdir = os.path.join("database", self.project.language)

        # Check if the storage directory exists
        os.makedirs(sdir, exist_ok=True)

        # Create the storage file
        sfile = os.path.join(sdir, f"{self.project.name}.json")

        # Check if the storage file exists
        if not os.path.exists(sfile):
            # Create the storage file
            with open(sfile, "w") as f:
                f.write("{}")

        # Get the project data and set the project data
        with open(sfile, "r") as f:
            data = json.load(f)
            data[self.project.name] = {
                "description": self.project.description,
                "path": self.project.path
            }

        # Write the project data
        with open(sfile, "w") as f:
            json.dump(data, f, indent=4)

        # Print the success message
        print("Successfully tracked the project!")



if __name__ == "__main__":
    tracker = Tracker()