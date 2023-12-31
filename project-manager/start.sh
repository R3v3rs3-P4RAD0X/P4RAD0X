#!/bin/bash

commands=(
    "tracker"
    "creator"
)

echo "Welcome to the project manager!"
echo "What would you like to do?"
echo ""

# Print the options with a number
for i in "${!commands[@]}"; do
    printf "%s\t%s\n" "$i" "${commands[$i]}"
done

echo ""
# Read the user input
read -p "Enter the number of the command you want to run: " input

# Check if the input is a number
if [[ $input =~ ^[0-9]+$ ]]; then
    # Check if the input is in the range of the array
    if [ $input -ge 0 ] && [ $input -lt ${#commands[@]} ]; then
        # Match the input with the command
        case $input in
            0)
                # Clear the screen
                clear
                
                # Run the tracker
                python tracker.py
                ;;
            1)
                # Clear the screen
                clear

                # Run the creator
                python main.py
                ;;
        esac
    else
        echo "Invalid input!"
    fi
else
    echo "Invalid input!"
fi
