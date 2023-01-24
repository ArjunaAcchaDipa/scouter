import basic_command

def scan(target, thread, is_default, current_time, is_verbose):
    output_file= f"dirsearch_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)
    
    thread = default_check(is_default, thread)
    
    if is_verbose:
        print("[+] Running dirsearch scan\n")

    # -u    --> target's url/ip
    # -t    --> threads
    # -r    --> recursive
    # -e    --> extension
    # -x    --> exclude status-code

    basic_command.run_command(f"sudo dirsearch -u {target} -e php,html,js,txt,sql -t {thread} -r -x 402-999 --format plain -o {output_file}")
    basic_command.run_command(f"cat /usr/lib/python3/dist-packages/dirsearch/{output_file} > {output}")

    result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")
        
    return result

def default_check(is_default, thread):
    default_thread = "50"

    if is_default:
        thread = default_thread 
    elif thread == "":
        thread = basic_command.input_timeout("\n[-] Thread for dirsearch (timeout in 60 seconds): ")
        if thread == "default" or thread == "":
            thread = default_thread
            print(f"[!] dirsearch thread will be set to {thread} because no thread were inputted\n")
    
    return thread