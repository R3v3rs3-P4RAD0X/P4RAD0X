#!/bin/bash

# This file installs some basic packages.
# Used to continue the setup process.

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Create a variable to store the current user's shell
current_shell=$(echo $SHELL)

# Check if the user's shell is bash
if [ "$current_shell" != "/bin/bash" ]; then
    # Change the user's shell to bash
    chsh -s /bin/bash
fi

# Create a list of packages
packages=(
    "git"
    "base-devel"
    "wget"
    "curl"
    "neovim"
    "python"
    "python-pip"
)

# Loop through the packages and install them
for package in "${packages[@]}"; do
    # Check if the package is installed
    if pacman -Qi $package &> /dev/null; then
        echo "$package is already installed"
    else
        # Install the package
        sudo pacman -S $package --noconfirm
    fi
done

# Change into the src directory
cd src

# Check if there's a .env directory
if [ ! -d ".env" ]; then
    # Create a virtual environment
    python -m venv .env
fi

# Activate the virtual environment
source .env/bin/activate

# Check if there's a requirements.txt file
if [ -f "requirements.txt" ]; then
    # Install the requirements
    pip install -r requirements.txt
fi

# Clear the screen
clear

# Print a message to the user
echo "Pre-setup is complete. Running main.py..."

# Run the main.py file
python main.py

# Deactivate the virtual environment
deactivate

# Go back a directory
cd ..

# Change the user's shell back to the original shell
chsh -s $current_shell