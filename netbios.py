import basic_command

def enumeration(target, port, current_time, is_verbose):
    output_file = f"netbios_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print("[+] Running NetBIOS Name Service enumeration")

    basic_command.run_command(f"nmblookup -A {target} > {output} && nmap --script nbstat -p{port} {target} >> {output}")

    result = basic_command.read_file(f"{output}")

    if is_verbose:
        print(result)

    return f"{result}"