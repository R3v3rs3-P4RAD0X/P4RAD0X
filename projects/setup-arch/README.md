# Setting up Arch

This project will automatically setup Arch linux based distros.
It's pre-configured and primarily made for my OS.

## Usage

To run this project use the following command:

```bash
sudo chmod +x setup.sh && ./setup.sh
```

## Useful Information

This script will overwrite these files;

#### /etc/sudoers

#### /etc/ssh/sshd_config

This script overwrites the basic config file for ssh. If you don't specify a port inside of main.py it will generate the file with a random port. This script also makes ssh accessible only using key based authentication on the root user.