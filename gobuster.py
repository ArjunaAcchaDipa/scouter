import basic_command

def scan(target, thread, wordlist, current_time, is_directory_scan, is_subdomain_scan, is_verbose):
    if is_directory_scan:
        output = f"gobuster_directory_{target}.txt"
    elif is_subdomain_scan:
        output = f"gobuster_subdomain_{target}.txt"
        
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)

    # check default variable(s)
    scan_type, wordlist, thread = default_check(wordlist, thread, is_directory_scan, is_subdomain_scan)

    # dir   --> to scan directory
    # vhost --> to scan subdomain
    # -u    --> target's url/ip
    # -w    --> wordlist
    # -t    --> thread
    # -k    --> Skip TLS certificate verification
    
    basic_command.run_command(f"gobuster {scan_type} -u {target} -w {wordlist} -t {thread} -k {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

def default_check(wordlist, thread, is_directory_scan, is_subdomain_scan):
    # getting data from .env file
    default_scan_directory_wordlist = ""
    default_scan_subdomain_wordlist = ""
    default_thread = "10"

    if is_directory_scan:
        scan_type = "dir"
        if wordlist == "":
            wordlist = input("Wordlist for Directory Scan: ")
    elif is_subdomain_scan:
        scan_type = "vhost"
        if wordlist == "":
            wordlist = input("Wordlist for Subdomain Scan: ")
    
    if thread == "":
        thread = 10

    return scan_type, wordlist, thread