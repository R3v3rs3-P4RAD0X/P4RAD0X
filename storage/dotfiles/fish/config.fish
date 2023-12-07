# Clear screen
clear

# Print welcome message
echo "Welcome back, $USER!" | lolcat

# Top of file
neofetch | lolcat 

# Source PATH
set -x PATH $PATH:/usr/local/bin:$HOME/.cargo/bin

# Aliases
alias ls "exa --all --long --header --color=auto --group-directories-first"
alias l "ls"
alias cat "bat"
alias c "clear"
alias mkdir "mkdir -pv"
alias copilots "gh copilot suggest"
alias copilote "gh copilot explain"

# Start ssh agent
eval (ssh-agent -c) > /dev/null

# Add ssh keys
for key in $HOME/.ssh/*
    if not string match --quiet "*.pub" $key
        if string match --quiet "*_ed25519" $key
            ssh-add -q $key
        end
    end
end

# Initialize starship
starship init fish | source
