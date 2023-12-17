#!/bin/bash

# This script makes it easier to run the dotfiles script.
python -u main.py | tee -a log.txt

# Alert the user that the script has finished.
echo "Finished running the dotfiles script."

# Tell the user there's a log file
echo "See 'log.txt' for more details."

# Exit the script.
exit 0
