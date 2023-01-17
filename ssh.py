import basic_command

def enumeration(target, port, current_time, is_verbose):
    output_file = f"ssh_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print("[+] Running SSH enumeration\n")

    basic_command.run_command(f"nmap -p{port} {target} -Pn --script ssh2-enum-algos,ssh-hostkey,ssh-auth-methods --script-args ssh_hostkey=full,ssh.user=root -oN {output}")

    result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")

    return result