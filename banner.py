def banner():
    print(" _____                 _             ")
    print("|   __| ___  ___  _ _ | |_  ___  ___ ")
    print("|__   ||  _|| . || | ||  _|| -_||  _|")
    print("|_____||___||___||___||_|  |___||_|  ")
    print("                                     ")
    print("=====================================")
    print("")

def help():
    print("Usage: python3 scouter.py -h [IP / URL] [Options]")
    
    print("")
    print("   -h, --host\tThe target IP or URL")
    print("   -p, --port\tOnly scan specified ports")
    print("      Ex: -p 80; -p 1-1000; -p 1-65535; -p all")

    print("   -t, --thread\tNumber of concurrent threads (default 50)")
    print("       --enum4linux-wordlist\tPath to the enum4linux wordlist")
    print("       --ftp-wordlist\tPath to the FTP wordlist")
    print("       --dir-wordlist\tPath to the Directory Scan wordlist")
    print("       --subdomain-wordlist\tPath to the Subdomain Scan wordlist")
    print("       --shodan-api\tThe Shodan API Token")
    print("       --virustotal-api\tThe VirusTotal API Token")

    print("")
    print("Flags:")
    print("   -d, --default\tdefault for wordlist and thread")
    print("   -v, --verbose\tVerbose output (results)")

def error_options():
    print("[!] Wrong input parameter!")
    print("[-] Example:")
    print("   [>] python3 scouter.py -h 192.168.0.1 -p 1-1000")
    print("   [>] python3 scouter.py -h www.google.com -p 1-1000")
    print("   [>] python3 scouter.py -h www.google.com -p all -v")
    print("   [>] python3 scouter.py -h www.google.com -p 1-65535 --enum4linux-wordlist /usr/share/enum4linux/share-list.txt")

def empty_options():
    print("[-] Example:")
    print("   [>] python3 scouter.py -h 192.168.0.1 -p 1-1000")
    print("   [>] python3 scouter.py -h www.google.com -p 1-1000")
    print("   [>] python3 scouter.py -h www.google.com -p all -v")
    print("   [>] python3 scouter.py -h www.google.com -p 1-65535 --enum4linux-wordlist /usr/share/enum4linux/share-list.txt")
    print("")
    print("[-] Auto Run:")
    print("   [>] python3 scouter.py -h 192.168.0.1 -d")