import traceback
import os


class CreationError(Exception):

    # Create a constructor with super
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.__class__.__name__}: ({self.get_error_location()}) {self.args[0]}"
    
    def __repr__(self):
        return str(self)
    
    def get_error_location(self):
        # Get the line number of the error and file name
        tb = traceback.extract_tb(self.__traceback__)[-1]
        filename = tb.filename.replace(os.getcwd() + "/", "")
        line = tb.lineno
        func = tb.name

        return f"File: {filename}, Line: {line}, Caller: {func}"
    


# Testing
if __name__ == "__main__":
    try:
        raise CreationError("This is a test")
    except CreationError as e:
        print(e)