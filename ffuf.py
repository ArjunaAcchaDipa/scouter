import basic_command

def scan(target, current_time, is_verbose):
    output_file = f"ffuf_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"ffuf -u {target} -w {wordlist} {basic_command.verbose_level(is_verbose)} {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"