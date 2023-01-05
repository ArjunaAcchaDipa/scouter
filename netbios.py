import basic_command

def enumeration(target, current_time, is_verbose):
    output_file = f"netbios_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nmblookup -A {target} > {output} && nmap --script nbstat -p137 {target} >> {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"