import basic_command

def scan(target, port, current_time, is_verbose):
    output = f"nmap_{target}.txt"
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)

    port = default_check(port)

    # -A        --> Enable OS detection, version detection, script scanning, and traceroute
    # -p        --> Port range
    # --script  --> script scan
    # vulners   --> scripts to scan vulnerability
    # -T4       --> timing template set to 4 (higher is faster)
    # -Pn       --> Treat all hosts as online (skip host discovery)

    basic_command.run_command(f"nmap -A -p{port} --script vulners -T4 {target} -Pn {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

    return f"{output_directory}{output}"

def default_check(port):
    if port == "":
        return "1-1000"
    elif port == "all":
        return "1-65535"
    else:
        return port