#!/bin/bash

# A simple script that works as a menu
# for the other scripts in this directory.

# The menu options.
options=(
    "Exit"
    "Project Creator"
)

project_creator() {
    # This will run the project creator script.
    # First change into the project-alpha directory.
    cd project-alpha

    # Run the project creator script using cargo.
    cargo run

    # Change back to the main directory.
    cd ..

    # New line
    echo ""

    # Ask the user if they're done or want to run another script.
    echo "Would you like to run another script? (y/N)"

    # Read the user input.
    read -r option

    # Check if the user wants to run another script.
    if [[ "$option" == "y" || "$option" == "Y" ]]; then
        # Call the menu function.
        display
    else
        # Exit the script.
        exit 0
    fi
}

# The menu function.
menu() {
    echo "Select an option:"

    # Print the menu options.
    for i in "${!options[@]}"; do
        printf "%s\t%s\n" "$i" "${options[$i]}"
    done

    echo ""

    # Read the user input.
    read -r option

    # Call the selected script.
    case "$option" in
        0) exit 0 ;;
        1) project_creator ;;
        *) echo "Invalid option." ;;
    esac
}

display() {
    # Clear the screen
    clear

    # Get the user's name
    name=$(whoami)

    # Print a welcome message.
    echo "Welcome, $name!"
    
    # Echo a small description about the script.
    echo "This script is a menu for running other scripts in this directory."

    # New line
    echo ""

    menu
}

# Call the display function.
display
