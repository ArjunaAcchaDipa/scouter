import abc
import basic_command

from getopt import getopt
import sys
import time

def auto(host, port, wordlist, thread, tools, is_verbose):
    pass

def default(host, port, wordlist, thread, tools, is_verbose):
    pass

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

    # !! Might be converted to call a function rather than using a flag
    # tools
    tool_dig = False
    tool_dnsenum = False
    tool_enum4linux = False
    tool_gobuster = False
    tool_nikto = False
    tool_nmap = False
    tool_searchsploit = False
    tool_shodan = False
    tool_virustotal = False
    tool_whois = False
    tool_wpscan = False

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

    if tools == "":
        tool_dig = True
        tool_dnsenum = True
        tool_whois = True
    elif tools == "auto":
        auto(host, port, wordlist, thread, tools, is_verbose)
    else:
        try:
            for tool in tools.split(","):
                if "dig" in tool:
                    tool_dig = True
                elif "dnsenum" in tool:
                    tool_dnsenum = True
                elif "enum4linux" in tool:
                    tool_enum4linux = True
                elif "gobuster" in tool:
                    tool_gobuster = True
                elif "nikto" in tool:
                    tool_nikto = True
                elif "nmap" in tool:
                    tool_nmap = True
                elif "searchsploit" in tool:
                    tool_searchsploit = True
                elif "shodan" in tool:
                    tool_shodan = True
                elif "virustotal" in tool:
                    tool_virustotal = True
                elif "whois" in tool:
                    tool_whois = True
                elif "wpscan" in tool:
                    tool_wpscan = True
        except Exception as e:
            print("[!] There is something wrong!")
            print(e)

if __name__ == "__main__":
    main()