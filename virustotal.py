import basic_command
import base64

# ! Validate api key

def scan(target, is_ip, is_url, api_key, current_time, is_verbose):
    output = f"virustotal_{target}.txt"
    output_directory = f"./result/{current_time}/"

    basic_command.mkdir(output_directory)

    if is_url and not is_ip:
        url_in_base64 = base64.urlsafe_b64encode(target.encode()).decode().strip('=')

        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/urls/{url_in_base64} --header 'x-apikey: {api_key}' {basic_command.verbose_level(is_verbose)} {output_directory}{output}")

    elif is_ip and not is_url:
        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/ip_adresses/{target} --header 'x-apikey: {api_key}' {basic_command.verbose_level(is_verbose)} {output_directory}{output}")