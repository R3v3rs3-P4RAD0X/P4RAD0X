# Imports
import random
import re
import string


# Passwd class
class Passwd:
    """
    Passwd class
    """

    def __init__(self) -> None:
        """
        Passwd class constructor
        """
        self.passwd = None

        # Minimum length of password
        self.min = 8
        self.max = 256

        # Password length
        self.length = 18

        # Password characters
        self.chars = string.ascii_letters + string.digits + string.punctuation

        # Regex for different levels of secure
        self.regex = {
            # Weak, must have a minimum of 8 characters and at least one number
            "weak": r"^(?=.*\d).{8,}$",
            # Medium, must have a minimum of 8 characters, at least one number and one special character and one upper and one lower case letter
            "medium": r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$",
            # Strong, must have a minimum of 16 characters, 4 numbers, 4 special characters and 4 upper and 4 lower case letters
            "strong": r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).{16,}$",
        }

    def generate(self, length: int = None) -> str:
        """
        Generate password
        """
        if length is None:
            length = self.min

        self.passwd = "".join(random.choice(self.chars) for _ in range(length))

        return self.passwd

    def test(self, passwd: str = None, level: str = "weak") -> bool:
        """
        Test password
        """
        if passwd is None:
            passwd = self.passwd

        return re.match(self.regex[level], passwd) is not None

    def max_complexity(self, passwd: str) -> str:
        """
        Checks against all regex and returns the highest one
        """

        for level in self.regex:
            if self.test(passwd, level):
                return level

        return "unknown"
    
    def to_complexity(level: str = "weak", passwd: str) -> str:
        """
        Converts a password to a specific complexity
        """
        if level == "weak":
            return passwd[:8]
        elif level == "medium":
            return passwd[:12]
        elif level == "strong":
            return passwd[:16]
        else:
            return passwd


# Testing
if __name__ == "__main__":
    passwd = Passwd()
    passwd.generate(18)
    print(passwd.passwd)
    print(passwd.test(passwd.passwd, "weak"))
    print(passwd.max_complexity(passwd.passwd))
