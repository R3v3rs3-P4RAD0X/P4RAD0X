"""
This file handles all pacman related tasks.
"""

# Imports
from system import System


# Pacman class
class Pacman:
    verbose: bool = False
    quiet: bool = True
    devnull: bool = True

    @staticmethod
    def install(*packages) -> list[str] | None:
        """
        Installs packages.

        :param packages: The packages to install.
        """
        # Check which packages are installed
        missing = []
        upgradable = []

        for package in packages:
            if not Pacman.isInstalled(package):
                missing.append(package)

            elif Pacman.isUpgradable(package):
                upgradable.append(package)

            else:
                continue

        # If missing is empty, return
        if len(missing) == 0 and len(upgradable) == 0:
            return

        # Install missing packages
        if len(missing) > 0:
            System.call(
                " ".join(
                    [
                        "pacman -Sy",
                        "--quiet" if Pacman.quiet else "",
                        "--verbose" if Pacman.verbose else "",
                        "--noconfirm",
                        " ".join(missing),
                        "> /dev/null 2>&1" if Pacman.devnull else "",
                    ]
                )
            )

        # Return
        return upgradable

    @staticmethod
    def update(package: str):
        """
        Updates the provided package.
        """
        # Check if the package is installed
        if not Pacman.isUpgradable(package):
            return

        # Update the package
        System.call(
            " ".join(
                [
                    "pacman -Syu",
                    "--quiet" if Pacman.quiet else "",
                    "--verbose" if Pacman.verbose else "",
                    "--noconfirm",
                    package,
                    "> /dev/null 2>&1" if Pacman.devnull else "",
                ]
            )
        )

    @staticmethod
    def isInstalled(package: str) -> bool:
        """
        Checks if a package is installed.

        :param package: The package to check.
        :return: Whether the package is installed.
        """
        return System.call(
            " ".join(
                [
                    "pacman -Q",
                    "--quiet" if Pacman.quiet else "",
                    "--verbose" if Pacman.verbose else "",
                    package,
                    "> /dev/null 2>&1" if Pacman.devnull else "",
                ]
            )
        )

    def isUpgradable(package: str) -> bool:
        """
        Checks if a package is upgradable.

        :param package: The package to check.
        :return: Whether the package is upgradable.
        """
        return System.call(
            " ".join(
                [
                    "pacman -Qu",
                    "--quiet" if Pacman.quiet else "",
                    "--verbose" if Pacman.verbose else "",
                    package,
                    "> /dev/null 2>&1" if Pacman.devnull else "",
                ]
            )
        )
    
    def upgradeAll(self) -> None:
        """
        Upgrades all packages.
        """
        System.call(
            " ".join(
                [
                    "pacman -Syyu",
                    "--quiet" if Pacman.quiet else "",
                    "--verbose" if Pacman.verbose else "",
                    "--noconfirm",
                    "> /dev/null 2>&1" if Pacman.devnull else "",
                ]
            )
        )