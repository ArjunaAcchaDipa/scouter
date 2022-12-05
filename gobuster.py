import basic_command

# default variable
default_wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
default_thread = 10

def scan_dir(target, thread, wordlist, current_time):
    if wordlist == "":
        wordlist = default_wordlist
    
    if thread == "":
        thread = default_thread
    
    output = f"gobuster_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/gobuster/"

    basic_command.mkdir(output_directory)

    # dir   --> to scan directory
    # vhost --> to scan subdomain
    # -u    --> target's url/ip
    # -w    --> wordlist
    # -t    --> thread
    # -o    --> output file

    basic_command.run_command(f"gobuster dir -u {target} -w {wordlist} -t {thread} -o {output_directory}{output}")