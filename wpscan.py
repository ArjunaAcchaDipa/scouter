import basic_command

def scan(target, current_time, is_verbose):
    output_file = f"wpscan_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"wpscan --url {target} -e > {output}")

    result = basic_command.read_file(f"{output}")
    
    if is_verbose:
        print (result)
    
    return f"{result}"