class CreationError(Exception):
    """
    Exception raised when an error occurs during creation.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CreationError: {self.message}"

    def __repr__(self) -> str:
        return self.__str__()

    # A function to get the line and file where the error occurred.
    # This is useful for debugging.
    def get_file(self) -> str:
        """
        Returns the line and file where the error occurred.

        Returns:
            str: The line and file where the error occurred.
        """

        return f"{self.__traceback__.tb_lineno} in {self.__traceback__.tb_frame.f_code.co_filename}"

    def get_name(self) -> str:
        """
        Returns the name of the function that the error occurred in.

        Returns:
            str: The name of the function that the error occurred in.
        """

        return self.__traceback__.tb_frame.f_code.co_name


# Testing
if __name__ == "__main__":
    try:
        raise CreationError("Testing")
    except CreationError as e:
        print(e)
        print(e.get_file())
        print(e.get_name())
