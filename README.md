# Scouter

**Scouter** is an automation application designed to perform various types of **reconnaissance** that are usually run manually one by one. This application can be run through a terminal on Kali Linux where the results of the reconnaissance will be compiled into a report.


## Table of Contents
* [Prerequisite and Technology](#prerequisite-and-technology)
* [Installation](#installation)
* [Command Description](#command-description)
* [Command Example](#command-example)

## Prerequisite and Technology
- Python 3 libraries
    - getopt
    - sys
    - time
    - subprocess
    - re
    - base64
    - python-decouple
    - docx-mailmerge
- Tools
    - DiG
    - dnsenum
    - dirsearch
    - enum4linux
    - Wget
    - Gobuster
    - Nmap
    - nmblookup
    - Nikto
    - seachsploit
    - Curl
    - WAFW00F
    - WhatWeb
    - whois
    - WPScan
    - abiword
- API
    - virustotal
    - shodan


## Installation

From your command line, clone and run **Scouter**:
```bash
$ git clone https://github.com/ArjunaAcchaDipa/Scouter.git

# Change directory using your terminal or cmd.
$ cd Scouter/

# Run the install.sh file
$ ./install.sh

# Run command export so the Gobuster can be used
$ export PATH=$PATH:~/go/bin

# Change the data in .env
# Re-open the terminal to refresh the installation

# Run the program using python 3
$ python scouter.py
```

## Command Description

Usage: python3 scouter.py -h [IP / URL] [Options]
```
-h, --host    The target IP or URL
-p, --port    Only scan specified ports
   Ex: -p 80; -p 1-1000; -p 1-65535; -p all

-t, --thread                 Number of concurrent threads (default 50)
    --enum4linux-wordlist    Path to the enum4linux wordlist
    --ftp-wordlist           Path to the FTP wordlist
    --dir-wordlist           Path to the Directory Scan wordlist
    --subdomain-wordlist     Path to the Subdomain Scan wordlist
    --shodan-api             The Shodan API Token
    --virustotal-api         The VirusTotal API Token

Flags:
   -d, --default    default for wordlist and thread
   -v, --verbose    Verbose output (results)
```

## Command Example

```bash
# Can be personalized
$ python3 scouter.py -h 192.168.0.1 -p 1-1000
$ python3 scouter.py -h www.google.com -p 1-1000
$ python3 scouter.py -h www.google.com -p all -v
$ python3 scouter.py -h www.google.com -p 1-65535 --enum4linux-wordlist /usr/share/enum4linux/share-list.txt

# Auto Run
$ python3 scouter.py -h 192.168.0.1 -d
```