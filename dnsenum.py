import basic_command

def scan(target, current_time):
    output = f"dnsenum_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/wpscan/"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"dnsenum {target} > {output_directory}{output}")

def show_options(target, current_time, is_verbose, is_run):
    options = f"""
    dnsenum
    ---

    TARGET          {target}
    """
    print(options)

    if is_run:
        scan(target, current_time, is_verbose)