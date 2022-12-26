import basic_command

def scan(target, current_time, is_verbose):
    output = f"nikto_{target}.txt"
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nikto -h {target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")