import getopt
import sys
import subprocess
import time
import re
from decouple import config

def colors(color):
    if color == "red":
        return "\033[1;31m"
    elif color == "yellow":
        return "\033[1;33m"
    elif color == "green":
        return "\033[1;32m"
    elif color == "normal":
        return "\033[0m"

def gobuster_parse_command(command):
    host = ""
    thread = 10
    wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"

    options, _ = getopt(sys.argv[1:], "h:t:w:", ["host", "thread", "wordlist"])

    for key, value in options:
        if key in ["-h", "--host"]:
            host = value
        elif key in ["-t", "--thread"]:
            thread = value
        elif key in ["-w", "--wordlist"]:
            wordlist = value
    
    # locate wordlist and validate thread and host is valid

def run_command(command):
    print("run command")
    print(command)
    process = subprocess.Popen(args=command, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    result, error = process.communicate()

    print("command done running")

    if error != b"":
        return f"Error\n{error}"
    elif result != b"":
        return result.decode()
    elif result == b"":
        return ""

def mkdir(directory_location):
    print(f"[+] Creating directory for {directory_location}")
    result = run_command(f"mkdir -p {directory_location}")
    if (result.startswith("Error")):
        print(f"[!] There is something wrong - {result}")
    else:
        print(f"[+] The directory has been created!")

def filename_time():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())

def check_ip_url(host):
    # regex below to validate the host is in ip format or not
    if (re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)):
        is_ip = True
    else:
        is_ip = False

    # regex below to validate the host is in url format or not
    if (re.search("(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", host)):
        is_url = True
    else:
        is_url = False
    
    return is_ip, is_url

def verbose_level(isVerbose):
    if isVerbose:
        return "| tee"
    else:
        return ">"

def read_file(filename):
    f = open(filename, "r")
    result = f.read()
    f.close()
    return result

def get_data_from_env(env_data):
    return config(env_data)