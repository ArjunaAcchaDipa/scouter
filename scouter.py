import basic_command, banner, report
import dig, dirsearch, dnsenum, enum4linux, gobuster, nikto, nmap, google, searchsploit, shodan_scan, virustotal, wafw00f, whatweb, whois, wpscan
import ftp, ssh, pop, netbios, ldap, mssql, mysql

from getopt import getopt
import sys
import time

def auto_scan(host, port, is_default, thread, enum4linux_wordlist, ftp_wordlist, gobuster_dir_wordlist, gobuster_subdomain_wordlist,  shodan_api, virustotal_api, filename_timestamp, is_verbose):
    # initial data
    nmap_result = nmap.scan(host, port, filename_timestamp, is_verbose)
    dig_result = dig.scan(host, filename_timestamp, is_verbose)
    dnsenum_result = dnsenum.scan(host, filename_timestamp, is_verbose)
    gdorks_result = google.dorks(host, filename_timestamp, is_verbose)
    virustotal_result = virustotal.scan(host, virustotal_api, filename_timestamp, is_verbose)
    shodan_result = shodan_scan.scan(host, shodan_api, filename_timestamp, is_verbose)
    searchsploit_result = searchsploit.scan(host, filename_timestamp, is_verbose)
    whois_result = whois.scan(host, filename_timestamp, is_verbose)

    open_ports = basic_command.get_substring("\d+\/.* open .*", nmap_result)        

    ftp_result = ""
    ssh_result = ""
    dirsearch_result = ""
    directory_result = ""
    subdomain_result = ""
    nikto_result = ""
    pop_result = ""
    enum4linux_result = ""
    netbios_result = ""
    ldap_result = ""
    mssql_result = ""
    mysql_result = ""
    wafw00f_result = ""
    whatweb_result = ""
    wpscan_result = ""

    for open_port in open_ports:
        # '80', 'tcp open  http    Apache httpd 2.4.18 ((Ubuntu))'
        port = open_port.split("/")[0]
        # ['80/tcp', 'open', '', 'http', '', '', '', 'Apache', 'httpd', '2.4.18', '((Ubuntu))']
        service = open_port.split(" ")[3].lower()

        if service == "ftp" and ftp_result == "":
            ftp_result = ftp.enumeration(host, is_default, filename_timestamp, ftp_wordlist, is_verbose)

        if service == "ssh" and ssh_result == "":
            ssh_result = ssh.enumeration(host, port, filename_timestamp, is_verbose)

        if "http" in service and directory_result == "":
            whatweb_result = whatweb.scan(host, filename_timestamp, is_verbose)

            # gobuster.scan(target, thread, is_default, current_time, scan_type, wordlist, is_verbose)
            directory_result = gobuster.scan(host, thread, is_default, filename_timestamp, "directory", gobuster_dir_wordlist, is_verbose)
            subdomain_result = gobuster.scan(host, thread, is_default, filename_timestamp, "subdomain", gobuster_subdomain_wordlist, is_verbose)

            dirsearch_result = dirsearch.scan(host, thread, is_default, filename_timestamp, is_verbose)
            
            nikto_result = nikto.scan(host, filename_timestamp, is_verbose)

            wafw00f_result = wafw00f.scan(host, service, filename_timestamp, is_verbose)

        if "pop" in service and pop_result == "":
            pop_result = pop.enumeration(host, port, filename_timestamp, is_verbose)

        if (service == "netbios-ssn" or service == "microsoft-ds") and enum4linux_result == "":
            enum4linux_result = enum4linux.scan(host, is_default, filename_timestamp, enum4linux_wordlist, is_verbose)
        
        if (service == "microsoft-ns" or service == "microsoft-dgm" or service == "netbios-ssn") and netbios_result == "":
            netbios_result = netbios.enumeration(host, port, filename_timestamp, is_verbose)
        
        if service == "ldap" and ldap_result == "":
            ldap_result = ldap.enumeration(host, port, filename_timestamp, is_verbose)
        
        if ("ms-sql" in service or "mssql" in service) and mssql_result == "":
            mssql_result = mssql.enumeration(host, port, filename_timestamp, is_verbose)
        
        if service == "mysql" and mysql_result == "":
            mysql_result = mysql.enumeration(host, port, filename_timestamp, is_verbose)
        
    if ("wp" in nmap_result.lower() or "wordpress") in nmap_result.lower():
        wpscan_result = wpscan.scan(host, filename_timestamp, is_verbose)

    report.auto_report(host, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

def main():
    start = time.time()
    filename_timestamp = basic_command.filename_time()

    options, _ = getopt(sys.argv[1:], "h:p:t:dv", ["help", "host=", "port=", "thread=", "default", "verbose", "dirsearch-wordlist=", "enum4linux-wordlist=", "ftp-wordlist=", "dir-wordlist=", "subdomain-wordlist=", "shodan-api=", "virustotal-api="])

    is_help = False
    host = ""
    port = ""
    thread = 10
    is_default = False
    is_verbose = False

    # Wordlist
    enum4linux_wordlist = ""
    gobuster_dir_wordlist = ""
    gobuster_subdomain_wordlist = ""
    ftp_wordlist = ""


    # API Key
    shodan_api = ""
    virustotal_api = ""

    # Host Type (IP or URL)
    is_ip = False
    is_url = False

    banner.banner()

    try:
        for key, value in options:
            if key in ["--help"]:
                is_help = True
                banner.help()

            elif key in ["-h", "--host"]:
                host = value
                is_ip, is_url = basic_command.check_ip_url(host)
                if not is_ip and not is_url:
                    print("[!] Invalid IP or URL detected.")
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
                        for number in port.split("-"):
                            if int(number) < 1 or int(number) > 65535:
                                raise
                            else:
                                pass
                    elif "," in port:
                        pass
                    else:
                        raise
                except:
                    print("[!] Invalid Port detected.")
                    exit()
                # print(f"port: {port}")

            elif key in ["--enum4linux-wordlist"]:
                enum4linux_wordlist = value
                # print(f"enum4linux_wordlist: {enum4linux_wordlist}")

            elif key in ["--ftp-wordlist"]:
                ftp_wordlist = value
                # print(f"ftp_wordlist: {ftp_wordlist}")

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
        banner.error_options()
        exit()

    if host != "" and not is_help:
        auto_scan(host, port, is_default, thread, enum4linux_wordlist, ftp_wordlist, gobuster_dir_wordlist, gobuster_subdomain_wordlist, shodan_api, virustotal_api, filename_timestamp, is_verbose)
    elif not is_help:
        banner.empty_options()

    end = time.time()
    basic_command.elapsed_time(start, end)

if __name__ == "__main__":
    main()