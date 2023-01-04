import basic_command
import base64

def scan(target, is_ip, is_url, api_key, current_time, is_verbose):
    output_file = f"virustotal_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    api_key = default_check(api_key)

    if is_url and not is_ip:
        url_in_base64 = base64.urlsafe_b64encode(target.encode()).decode().strip('=')

        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/urls/{url_in_base64} --header 'x-apikey: {api_key}' {basic_command.verbose_level(is_verbose)} {output}")

    elif is_ip and not is_url:
        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/ip_adresses/{target} --header 'x-apikey: {api_key}' {basic_command.verbose_level(is_verbose)} {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"

def default_check(api_key):
    if api_key == "":
        api_key = input("API Key for VirusTotal: ")
    
    return api_key