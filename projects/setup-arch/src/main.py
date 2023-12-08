"""
This script will handle the rest of the setup process.
"""

# Imports #
from components import Pacman, Printer, SSHD, Sudoers
from system import System

# Main #
if __name__ == "__main__":
    # Print header
    Printer.header()

    # Create a new section
    Printer.log(Printer.format("📦\tInstalling packages...", colour="blue"))
    upgradable = Pacman.install(
        "git",
        "base-devel",
        "python",
        "python-pip",
        "linux",
        "linux-headers",
        "neofetch",
        "lolcat",
        "neovim",
        "yay",
        "fish",
    )
    
    # Check if the length of upgradable is greater than 0
    if upgradable and len(upgradable) > 0:
        # Create a new section
        for package in upgradable:
            # Print a warning about package not updated
            Printer.log(Printer.format(f"⚠️\t{package} not updated!", colour="yellow"))
            Pacman.update(package)
            Printer.log(Printer.format(f"✅\t{package} updated!", colour="green"))

    Printer.log(Printer.format("✅\tPackages installed!", colour="green"))
    Printer.empty()

    # Create a new section
    Printer.log(Printer.format("🔧\tConfiguring system...", colour="blue"))
    SSHD.create(Printer, port=None)
    Sudoers.create(Printer)
    Printer.log(Printer.format("✅\tSystem configured!", colour="green"))