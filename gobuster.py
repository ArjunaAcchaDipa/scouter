import basic_command

def scan(target, thread, wordlist, current_time, is_verbose):    
    output = f"gobuster_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/gobuster/"

    basic_command.mkdir(output_directory)

    # dir   --> to scan directory
    # vhost --> to scan subdomain
    # -u    --> target's url/ip
    # -w    --> wordlist
    # -t    --> thread
    # -o    --> output file
    
    basic_command.run_command(f"gobuster dir -u {target} -w {wordlist} -t {thread} -k {basic_command.verbose_level(is_verbose)} {output_directory}{output}")