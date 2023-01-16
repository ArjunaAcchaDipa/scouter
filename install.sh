#!/bin/bash

# Update the machine
sudo apt update -y

# Set golang configuration
. ./go.cfg

# Installing python
sudo apt install software-properties-common -y
sudo apt install python3.10 -y
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc

# Install python pip & library used
sudo apt install python3-pip -y
pip install -r ./requirements.txt

# Copy .env.example to .env
cp .env.example .env

# Download tools
sudo apt install git-all -y
sudo apt install dirsearch -y
sudo apt install dnsenum -y
sudo apt install enum4linux -y
sudo apt install nikto -y
sudo apt install nmap -y
sudo apt install wafw00f -y
sudo apt install whatweb -y
sudo apt install whois -y
sudo apt install ruby-full -y
sudo gem install wpscan

# Install golang & gobuster
sudo apt install golang-go -y
go install github.com/OJ/gobuster/v3@latest
# echo "export PATH=$PATH:~/go/bin" >> ~/.bashrc
# source ~/.bashrc
sudo ln -sf /usr/local/go/bin/go /usr/local/bin/
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$HOME/.local/bin:$PATH

# Tool to convert docx to pdf
sudo apt install abiword -y

# Give recommendation to close and re-open terminal
echo -e "\n\nRun this command in terminal:"
echo "export PATH=\$PATH:~/go/bin"
echo -e "\nAfter running export command"
echo "Try to re-open the terminal"
