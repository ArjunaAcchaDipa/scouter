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

def show_options(target, sharenames_wordlist, current_time, is_verbose, isRun):
    default_sharenames_wordlist = "/usr/share/enum4linux/share-list.txt"

    if sharenames_wordlist == "":
        sharenames_wordlist = default_sharenames_wordlist

    options = f"""
    enum4linux
    ----------

    TARGET          {target}

    Wordlist
    --------
    SHARENAMES      {sharenames_wordlist}
    """
    print(options)

    if isRun:
        scan(target, sharenames_wordlist, current_time, is_verbose)