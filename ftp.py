import basic_command

def enumeration(target, is_default, current_time, wordlist, is_verbose):
    output_response = f"ftp_response_{target}.txt"
    output_html = f"ftp_html_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_response}"

    basic_command.mkdir(output_directory)

    credentials = default_check(is_default, wordlist)

    if is_verbose:
        print("[+] Running ftp enumeration\n")

    for credential in credentials:
        basic_command.run_command(f"wget ftp://{credential}@{target} -o {output} -O {output_directory}{output_html}")

        result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

        if "Logged in" in result:
            break
    
    if "Logged in" not in result:
        result = "No credential matched"

    if is_verbose:
        print(f"{result}\n")

    return result

def default_check(is_default, wordlist):
    default_ftp_credentials = basic_command.read_file("./wordlist/ftp-betterdefaultpasslist.txt").split("\n")

    if is_default:
        wordlist = default_ftp_credentials
    elif wordlist == "":
        wordlist = basic_command.input_timeout("\n[-] Wordlist for FTP Credentials Wordlist (timeout in 60 seconds): ")
        if wordlist == "default" or wordlist == "":
            wordlist = default_ftp_credentials
            print(f"[!] ftp wordlist will be set to {wordlist} because no wordlist were inputted\n")
    
    return wordlist