import basic_command

def enumeration(target, port, current_time, is_verbose):
    output_file = f"ldap_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print("[+] Running ldap enumeration\n")

    basic_command.run_command(f"nmap -p{port} --script ldap-rootdse {target} -oN {output}")

    result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")

    return result