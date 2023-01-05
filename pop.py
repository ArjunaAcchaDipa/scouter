import basic_command

def enumeration(target, current_time, is_verbose):
    output_file = f"pop_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nmap --script \"pop3-capabilities or pop3-ntlm-info\" -sV -p110 {target} -oN {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"