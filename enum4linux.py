import basic_command

def scan(target, sharenames_wordlist, current_time, is_verbose):
    output = f"enum4linux_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/enum4linux/"

    basic_command.mkdir(output_directory)
    
    # -n --> nmblookup
    # -P --> get password policy information
    # -s --> brute force share names
    # -U --> get userlist

    basic_command.run_command(f"enum4linux -n -P -s {sharenames_wordlist} -U {target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")