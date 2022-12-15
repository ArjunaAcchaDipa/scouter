import basic_command

def scan(target, current_time, is_verbose):
    output = f"whois_{target}_{current_time}.txt"
    output_directory = f"./result/{current_time}/whois/"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"whois {target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")