import basic_command

def scan(target, is_default, current_time, wordlist, is_verbose):
    output_file = f"enum4linux_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    wordlist = default_check(is_default, wordlist)

    if is_verbose:
        print("[+] Running enum4linux scan")
    
    # -n --> nmblookup
    # -P --> get password policy information
    # -s --> brute force share names
    # -U --> get userlist

    basic_command.run_command(f"enum4linux -n -P -s {wordlist} -U {target} > {output}")

    result = basic_command.read_file(f"{output}")

    if is_verbose:
        print(result)
        
    return f"{result}"

def default_check(is_default, wordlist):
    default_wordlist = "./wordlist/share-list.txt"

    if is_default:
        wordlist = default_wordlist
    elif wordlist == "":
        wordlist = basic_command.input_timeout("Wordlist for enum4linux (timeout in 60 seconds): ")
        if wordlist == "default":
            wordlist = default_wordlist
            print(f"enum4linux wordlist will be set to {wordlist} because no wordlist were inputted")
    
    return wordlist