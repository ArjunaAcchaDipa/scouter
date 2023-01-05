import basic_command

def scan(target, thread, current_time, is_verbose, wordlist):
    # output_file
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    # -u    --> target's url/ip
    # -w    --> wordlists
    # -t    --> threads
    # -r    --> recursive

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"dirsearch -u {target} -w {wordlist} -t {thread} -r {basic_command.verbose_level(isVerbose)} {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"