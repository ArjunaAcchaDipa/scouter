import basic_command
import base64

def scan(target, api_key, current_time, is_verbose):
    output_file = f"virustotal_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    is_ip, is_url = basic_command.check_ip_url(target)
    api_key = default_check(api_key)

    if api_key.startswith("Skipping"):
        if is_verbose:
            print(f"[!] {api_key}\n")
        return api_key

    if is_verbose:
        print("[+] Running VirusTotal scan\n")

    if is_url and not is_ip:
        url_in_base64 = base64.urlsafe_b64encode(target.encode()).decode().strip('=')

        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/urls/{url_in_base64} --header 'x-apikey: {api_key}' > {output}")

    elif is_ip and not is_url:
        basic_command.run_command(f"curl --request GET --url https://www.virustotal.com/api/v3/ip_adresses/{target} --header 'x-apikey: {api_key}' > {output}")

    result = basic_command.read_file(f"{output}").lstrip("\n").rstrip("\n")

    if is_verbose:
        print(f"{result}\n")
        
    return result

def default_check(api_key):
    if api_key == "":
        api_key = basic_command.input_timeout("\n[-] API Key for VirusTotal (timeout in 60 seconds): ")
        if api_key == "default" or api_key == "":
            api_key = "Skipping VirusTotal because no API Key were inputted"
            print(f"\n[!] VirusTotal will be skipped because no API Key were inputted\n")
    
    return api_key