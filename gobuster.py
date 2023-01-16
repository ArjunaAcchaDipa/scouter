import basic_command

def scan(target, thread, is_default, current_time, scan_type, wordlist, is_verbose):
    # check default variable(s)
    output_file, thread, mode, wordlist = default_check(target, thread, is_default, scan_type, wordlist)
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print(f"[+] Running gobuster for {scan_type}")

    # dir   --> to scan directory
    # vhost --> to scan subdomain
    # -u    --> target's url/ip
    # -w    --> wordlist
    # -t    --> thread
    # -k    --> Skip TLS certificate verification
    
    basic_command.run_command(f"gobuster {mode} -u {target} -w {wordlist} -t {thread} -k > {output}")

    result = basic_command.read_file(f"{output}")

    if is_verbose:
        print(result)
        
    return f"{result}"

def default_check(target, thread, is_default, scan_type, wordlist):
    default_scan_directory_wordlist = "./wordlist/directory-list-2.3-medium.txt"
    default_scan_subdomain_wordlist = "./wordlist/subdomain-wordlist.txt"
    default_thread = "50"

    if scan_type == "directory":
        output = f"gobuster_directory_{target}.txt"
        mode = "dir"
    elif scan_type == "subdomain":
        output = f"gobuster_subdomain_{target}.txt"
        mode = "vhost"

    if is_default and scan_type == "directory":
        return output, default_thread, mode, default_scan_directory_wordlist
    elif is_default and scan_type == "subdomain":
        return output, default_thread, mode, default_scan_subdomain_wordlist
    elif not is_default:
        wordlist = basic_command.input_timeout("Wordlist for Directory/Subdomain Scan (timeout in 60 seconds): ")
        if wordlist == "default" and scan_type == "directory":
            wordlist = default_scan_directory_wordlist
            print(f"Gobuster wordlist for directory will be set to {wordlist} because no wordlist were inputted")
        elif wordlist == "default" and scan_type == "subdomain":
            wordlist = default_scan_subdomain_wordlist
            print(f"Gobuster wordlist for subdomain will be set to {wordlist} because no wordlist were inputted")

        thread = basic_command.input_timeout("Thread for Gobuster (timeout in 60 seconds): ")
        if thread == "default":
            thread = default_thread
            print(f"Gobuster thread will be set to {thread} because no API Key were inputted")

        return output, thread, mode, wordlist