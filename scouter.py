import basic_command

from getopt import getopt
import sys
from tabnanny import verbose
import time

def main():
    start = time.time()
    filename_timestamp = basic_command.filename_time()

    options, _ = getopt(sys.argv[1:], "h:p:w:t:T:v", ["host", "port", "wordlist", "thread", "tools", "verbose"])

    host = ""
    port = ""
    wordlist = ""
    thread = 10
    tools = ""
    is_verbose = False

    try:
        for key, value in options:
            if key in ["-h", "--host"]:
                host = value
            elif key in ["-p", "--port"]:
                port = value
            elif key in ["-w", "--wordlist"]:
                wordlist = value
            elif key in ["-t", "--thread"]:
                thread = value
            elif key in ["-T", "--tools"]:
                tools = value
            elif key in ["-v", "--verbose"]:
                is_verbose = True
    except:
        print("[!] Wrong input parameter!")



if __name__ == "__main__":
    main()