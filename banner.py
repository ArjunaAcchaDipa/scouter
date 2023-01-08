def banner():
    print(" _____                 _             ")
    print("|   __| ___  ___  _ _ | |_  ___  ___ ")
    print("|__   ||  _|| . || | ||  _|| -_||  _|")
    print("|_____||___||___||___||_|  |___||_|  ")
    print("                                     ")
    print("=====================================")

def error_options():
    print("[!] Wrong input parameter!")
    print("[-] Example:")
    print("\t[>] python3 scouter.py -h 192.168.0.1 -p 1-1000")
    print("\t[>] python3 scouter.py -h www.google.com -p 1-1000")
    print("\t[>] python3 scouter.py -h www.google.com -p all -w -v")
    print("\t[>] python3 scouter.py -h www.google.com -p 1-65535 --enum4linux-wordlist /usr/share/enum4linux/share-list.txt")