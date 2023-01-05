import basic_command

def enumeration(target, current_time, is_verbose):
    output_file = f"mysql_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nmap --script \"rdp-enum-encryption or rdp-vuln-ms12-020 or rdp-ntlm-info\" -p3389 {target} -oN {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"