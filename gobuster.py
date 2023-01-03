import basic_command

def scan(target, thread, is_default, current_time, scan_type, wordlist, is_verbose):
    # check default variable(s)
    output, thread, wordlist = default_check(target, thread, is_default, scan_type, wordlist)
        
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)


    # dir   --> to scan directory
    # vhost --> to scan subdomain
    # -u    --> target's url/ip
    # -w    --> wordlist
    # -t    --> thread
    # -k    --> Skip TLS certificate verification
    
    basic_command.run_command(f"gobuster {scan_type} -u {target} -w {wordlist} -t {thread} -k {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

def default_check(target, thread, is_default, scan_type, wordlist):
    # getting data from .env file
    default_scan_directory_wordlist = "./wordlist/directory-list-2.3-medium.txt"
    default_scan_subdomain_wordlist = "./wordlist/subdomain-wordlist.txt"
    default_thread = "10"

    if scan_type == "directory":
        output = f"gobuster_directory_{target}.txt"
    elif scan_type == "subdomain":
        output = f"gobuster_subdomain_{target}.txt"

    if is_default and scan_type == "directory":
        return output, default_thread, default_scan_directory_wordlist
    elif is_default and scan_type == "subdomain":
        return output, default_thread, default_scan_subdomain_wordlist
    elif not is_default:
        wordlist = input("Wordlist for Directory/Subdomain Scan: ")
        thread = input("Thread: ")
        return output, thread, wordlist