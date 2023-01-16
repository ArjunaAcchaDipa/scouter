import basic_command

def scan(target, port, current_time, is_verbose):
    output_file = f"nmap_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    port = default_check(port)

    if is_verbose:
        print("[+] Running Nmap for initial data")

    # -A        --> Enable OS detection, version detection, script scanning, and traceroute
    # -p        --> Port range
    # --script  --> script scan
    # vulners   --> scripts to scan vulnerability
    # -T4       --> timing template set to 4 (higher is faster)
    # -Pn       --> Treat all hosts as online (skip host discovery)

    basic_command.run_command(f"nmap -A -p{port} --script vulners -T4 {target} -Pn -oN {output}")

    result = basic_command.read_file(f"{output}")

    if is_verbose:
        print(result)

    return f"{result}"

def default_check(port):
    if port == "":
        return "1-1000"
    elif port == "all":
        return "1-65535"
    else:
        return port

def parsing_data(nmap_result):
    try:
        os_host = "".join(basic_command.get_substring("OS: \w+", nmap_result)).split(" ")[1].rstrip(";")
    except:
        os_host = "unknown host"
    
    return os_host