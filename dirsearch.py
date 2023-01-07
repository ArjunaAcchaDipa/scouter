import basic_command

def scan(target, thread, is_default, current_time, wordlist, is_verbose):
    output_file= f"dirsearch_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)
    
    wordlist = default_check(is_default, wordlist)

    # -u    --> target's url/ip
    # -w    --> wordlists
    # -t    --> threads
    # -r    --> recursive

    basic_command.run_command(f"dirsearch -u {target} -w {wordlist} -t {thread} -r {basic_command.verbose_level(is_verbose)} {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"

def default_check(is_default, wordlist):
    default_wordlist = "./wordlist/directory-list-2.3-medium.txt"

    if is_default:
        wordlist = default_wordlist
    elif wordlist == "":
        wordlist = input("Wordlist for dirsearch: ")
    
    return wordlist