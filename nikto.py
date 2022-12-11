import basic_command

def scan(target, current_time, is_verbose):
    output = f"nikto_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/nikto/"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nikto -h {target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

def show_options(target, current_time, is_verbose, is_run):
    options = f"""
    nikto
    -----

    TARGET          {target}
    """
    print(options)

    if is_run:
        scan(target, current_time, is_verbose)