import basic_command

# default variable
default_wordlist = "/usr/share/enum4linux/share-list.txt"

def scan(target, wordlist, current_time, isVerbose):
    if wordlist == "":
        wordlist = default_wordlist

    output = f"enum4linux_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/enum4linux/"

    basic_command.mkdir(output_directory)
    
    # -n --> nmblookup
    # -P --> get password policy information
    # -s --> brute force share names
    # -U --> get userlist

    basic_command.run_command(f"enum4linux -n -P -s /usr/share/enum4linux/share-list.txt -U {target} {basic_command.verbose_level(isVerbose)} {output_directory}{output}")