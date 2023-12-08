"""
This file will handle the creating of the sshd_config file.
"""

import os
import random

# Imports
from system import System


# SSHD class
class SSHD:
    def __init__(self):
        raise Exception("This class cannot be instantiated.")

    @staticmethod
    def create(Printer, port: int = None, key_based: bool = False) -> None:
        """
        Creates the sshd_config file.
        """
        # Create the sshd_config file
        System.call("cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak")

        # Get the template file
        template = System.readFile(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "template_files", "sshd_config.txt"
                )
            )
        )

        # Check if port was not provided
        if port is None or type(port) != int:
            # Generate a random port
            port = random.randint(1024, 65535)

            # Check if the port is in use using netstat -tulpn
            while len(System.call_output(f"netstat -tulpn | grep {port}")) > 0:
                # Generate a new port
                port = random.randint(1024, 65535)

        # Replace the port in the template
        template = template.replace("{port}", str(port))

        # Check if key based authentication is enabled
        template = template.replace("{pub_key}", "yes" if key_based else "no")
        template = template.replace("{pass_auth}", "no" if key_based else "yes")

        # Write the template to the sshd_config file
        with open("/etc/ssh/sshd_config", "w") as file:
            file.write(template)

        # Restart the sshd service
        System.call("systemctl restart sshd")

        # Print a success message
        Printer.log(
            Printer.format(f"✅\tSSHD Config created! Port: ({port})", colour="green")
        )
