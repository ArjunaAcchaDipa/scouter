import basic_command

def enumeration(target, current_time, is_verbose):
    output_file = f"ssh_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nmap -p22 {target} --script ssh2-enum-algos --script ssh-hostkey --script-args ssh_hostkey=full --script ssh-auth-methods --script-args=\"ssh.user=root\" -oN {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"