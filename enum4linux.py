import basic_command

def scan(target, wordlist, current_time, is_verbose):
    output = f"enum4linux_{target}.txt"
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)

    wordlist = default_check(wordlist)
    
    # -n --> nmblookup
    # -P --> get password policy information
    # -s --> brute force share names
    # -U --> get userlist

    basic_command.run_command(f"enum4linux -n -P -s {wordlist} -U {target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

def default_check(wordlist):
    default_wordlist = ""

    if wordlist == "":
        wordlist = input("Wordlist for enum4linux: ")
    
    return wordlist