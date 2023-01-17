import basic_command

def enumeration(target, port, current_time, is_verbose):
    output_file = f"mysql_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    if is_verbose:
        print("[+] Running mysql enumeration\n")

    basic_command.run_command(f"nmap -sV -p{port} --script mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 {target} -oN {output}")

    result = basic_command.read_file(output).lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")

    return result