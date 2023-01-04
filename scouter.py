import basic_command
import dig, dnsenum, enum4linux, gobuster, nikto, nmap, ftp, google, searchsploit, shodan, ssh, virustotal, whois, wpscan

from getopt import getopt
import sys
import time

def auto_scan(host, port, is_default, thread, enum4linux_wordlist, gobuster_dir_wordlist, gobuster_subdomain_wordlist, shodan_api, virustotal_api, filename_timestamp, is_verbose):
    nmap_filename = nmap.scan(host, port, filename_timestamp, is_verbose)
    nmap_result = basic_command.read_file(nmap_filename)

    if "21" in nmap_result or "ftp" in nmap_result:
        ftp_result = ftp.enumeration(host, filename_timestamp, is_verbose)

    if "22" in nmap_result or "ssh" in nmap_result:
        ssh_result = ssh.enumeration(host, filename_timestamp, is_verbose)

    if "80" in nmap_result or "443" in nmap_result or "http" in nmap_result:
        dig_result = dig.scan(host, filename_timestamp, is_verbose)
        dnsenum_result = dnsenum.scan(host, filename_timestamp, is_verbose)

        # gobuster.scan(target, thread, is_default, current_time, scan_type, wordlist, is_verbose)
        directory_result = gobuster.scan(host, thread, is_default, filename_timestamp, "directory", gobuster_dir_wordlist, is_verbose)
        subdomain_result = gobuster.scan(host, thread, is_default, filename_timestamp, "subdomain", gobuster_subdomain_wordlist, is_verbose)
        
        nikto_result = nikto.scan(host, filename_timestamp, is_verbose)

    if "135" in nmap_result or "139" in nmap_result or "445" in nmap_result or "smb" in nmap_result or "samba" in nmap_result or "Samba" in nmap_result:
        enum4linux_result = enum4linux.scan(host, enum4linux_wordlist, filename_timestamp, is_verbose)

def main():
    start = time.time()
    filename_timestamp = basic_command.filename_time()

    options, _ = getopt(sys.argv[1:], "h:p:t:dv", ["host", "port", "thread", "default", "verbose", "enum4linux-wordlist", "dir-wordlist", "subdomain-wordlist", "shodan-api", "virustotal_api"])

    host = ""
    port = ""
    wordlist = ""
    thread = 10
    is_default = False
    is_verbose = False

    # Wordlist
    enum4linux_wordlist = ""
    gobuster_dir_wordlist = ""
    gobuster_subdomain_wordlist = ""

    # API Key
    shodan_api = ""
    virustotal_api = ""

    # Host Type (IP or URL)
    is_ip = False
    is_url = False

    try:
        for key, value in options:
            if key in ["-h", "--host"]:
                host = value
                is_ip, is_url = basic_command.check_ip_url(host)
                if not is_ip and not is_url:
                    print("[!] Invalid IP or hostname detected.")
                    print("[-] Example:")
                    print("\t[>] 192.168.0.1")
                    print("\t[>] google.com")
                    exit()
                # print(f"host: {host}")

            elif key in ["-p", "--port"]:
                port = value
                try:
                    if port == "all":
                        pass
                    elif "-" not in port:
                        if int(port) >= 1 and int(port) <= 65535:
                            pass
                        else:
                            raise
                    elif "-" in port and port.count("-") == 1:
                        for number in int(port.split("-")):
                            if number < 1 or number > 65535:
                                raise
                            else:
                                pass
                    else:
                        raise
                except:
                    print("[!] Invalid Port detected.")
                    print("[-] Example:")
                    print("\t[>] 80")
                    print("\t[>] 443")
                    print("\t[>] 1-1000")
                    print("\t[>] 1-65535")
                    print("\t[>] all")
                    exit()
                # print(f"port: {port}")

            elif key in ["--enum4linux-wordlist"]:
                enum4linux_wordlist = value
                # print(f"enum4linux_wordlist: {enum4linux_wordlist}")

            elif key in ["--dir-wordlist"]:
                gobuster_dir_wordlist = value
                # print(f"gobuster_dir_wordlist: {gobuster_dir_wordlist}")

            elif key in ["--subdomain-wordlist"]:
                gobuster_subdomain_wordlist = value
                # print(f"gobuster_subdomain_wordlist: {gobuster_subdomain_wordlist}")
                
            elif key in ["-d", "--default"]:
                is_default = True
                # print(f"default_wordlist: {default_wordlist}")

            elif key in ["-t", "--thread"]:
                thread = value
                # print(f"thread: {thread}")

            elif key in ["-v", "--verbose"]:
                is_verbose = True
                # print(f"is_verbose: {is_verbose}")

            elif key in ["--shodan-api"]:
                shodan_api = value
                # print(f"shodan_api: {shodan_api}")

            elif key in ["--virustotal-api"]:
                virustotal_api = value
                # print(f"virustotal_api: {virustotal_api}") 

    except:
        print("[!] Wrong input parameter!")
        print("[-] Example:")
        print("\t[>] python3 scouter.py -h 192.168.0.1 -p 1-1000")
        print("\t[>] python3 scouter.py -h www.google.com -p 1-1000")
        print("\t[>] python3 scouter.py -h www.google.com -p all -w -v")
        print("\t[>] python3 scouter.py -h www.google.com -p 1-65535 --enum4linux-wordlist /usr/share/enum4linux/share-list.txt")
        exit()

    auto_scan(host, port, is_default, thread, enum4linux_wordlist, gobuster_dir_wordlist, gobuster_subdomain_wordlist, shodan_api, virustotal_api, filename_timestamp, is_verbose)

if __name__ == "__main__":
    main()