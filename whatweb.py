import basic_command

def scan(target, current_time, is_verbose):
    output_file = f"whatweb_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print("[+] Running WhatWeb scan\n")

    basic_command.run_command(f"whatweb {target} > {output}")

    result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")
        
    return result