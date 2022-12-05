import basic_command
import base64

# default variable
default_api_key = "27d57e1052de85b1cd2952fd3f8a4fdfb950c29cd7571bf6d584e290bc435808"

def scan(target, isIP, isURL, current_time):
    output = f"virustotal_{target}_{current_time}.txt"
    output_directory = f"./result/{current_time}/virustotal/"

    basic_command.mkdir(output_directory)

    if isURL:
        url_in_base64 = base64.urlsafe_b64encode(target.encode()).decode().strip('=')

        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/urls/{url_in_base64} --header 'x-apikey: {default_api_key}' > {output_directory}{output}")

    elif isIP:
        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/ip_adresses/{target} --header 'x-apikey: {default_api_key}' > {output_directory}{output}")