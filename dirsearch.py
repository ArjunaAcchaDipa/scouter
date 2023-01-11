import basic_command

def scan(target, thread, is_default, current_time, is_verbose):
    output_file= f"dirsearch_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)
    
    thread = default_check(is_default, thread)

    # -u    --> target's url/ip
    # -t    --> threads
    # -r    --> recursive
    # -e    --> extension
    # -x    --> exclude status-code

    basic_command.run_command(f"dirsearch -u {target} -e php,html,js,txt,sql -t {thread} -r -x 402-999 > {output}")

    result = basic_command.read_file(f"{output}")

    if is_verbose:
        print (result)
        
    return f"{result}"

def default_check(is_default, thread):
    default_thread = "50"

    if is_default:
        thread = default_thread 
    elif thread == "":
        thread = input("Thread for dirsearch: ")
    
    return thread