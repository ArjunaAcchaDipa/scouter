import basic_command

def scan(service_target, current_time, is_verbose):
    output = f"searchsploit_{target}_{current_time}.txt"
    output_directory = f"./result/current_time/searchsploit/"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"searchsploit {service_target} {basic_command.verbose_level(is_verbose)} {output_directory}{output}")