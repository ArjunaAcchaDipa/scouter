import basic_command

def enumeration(target, current_time, is_verbose):
    output_response = f"ftp_response_{target}.txt"
    output_html = f"ftp_html_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_response}"

    basic_command.mkdir(output_directory)

    default_ftp_credentials = basic_command.read_file("./wordlist/ftp-betterdefaultpasslist.txt").split("\n")

    for credential in default_ftp_credentials:
        basic_command.run_command(f"wget ftp://{credential}@{target} -o {output} -O {output_directory}{output_html}")

        result = basic_command.read_file(f"{output}")

        if "Logged in" in result:
            break

    return f"{result}"