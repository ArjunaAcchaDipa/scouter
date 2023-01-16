import subprocess
import time
import re
from decouple import config
from inputimeout import inputimeout

def colors(color):
    if color == "red":
        return "\033[1;31m"
    elif color == "yellow":
        return "\033[1;33m"
    elif color == "green":
        return "\033[1;32m"
    elif color == "normal":
        return "\033[0m"

def run_command(command):
    process = subprocess.Popen(args=command, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    result, error = process.communicate()

    if error != b"":
        return f"Error\n{error.decode()}"
    elif result != b"":
        return result.decode()
    elif result == b"":
        return ""

def mkdir(directory_location):
    result = run_command(f"mkdir -p {directory_location}")
    if (result.startswith("Error")):
        print(f"[!] There is something wrong - {result}")
    else:
        pass

def filename_time():
    return time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())

def current_date():
    return time.strftime("%B %d, %Y", time.localtime())

def check_ip_url(host):
    # regex below to validate the host is in ip format or not
    if (re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)):
        is_ip = True
    else:
        is_ip = False

    # regex below to validate the host is in url format or not
    if (re.search("(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", host)):
        is_url = True
    else:
        is_url = False
    
    return is_ip, is_url

def read_file(filename):
    f = open(filename, "r")
    result = f.read()
    f.close()

    try:
        ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")

        return ansi_escape.sub("", result)
    except:
        return result

def get_data_from_env(env_data):
    return config(env_data)

def get_substring(regex_used, full_text):
    return re.findall(regex_used, full_text)

def get_tools_used(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    tools = []

    if nmap_result != "":
        tools.append("nmap")

    if ftp_result != "":
        tools.append("ftp")

    if ssh_result != "":
        tools.append("ssh")

    if dig_result != "" or dnsenum_result != "":
        tools.append("dns lookup")

    if directory_result != "" or dirsearch_result != "":
        tools.append("directory scan")

    if subdomain_result != "":
        tools.append("subdomain scan")

    if nikto_result != "":
        tools.append("nikto")
    
    if wafw00f_result != "":
        tools.append("wafw00f")
    
    if whatweb_result != "":
        tools.append("whatweb")

    if pop_result != "":
        tools.append("pop")

    if enum4linux_result != "":
        tools.append("enum4linux")

    if netbios_result != "":
        tools.append("netbios")

    if gdorks_result != "":
        tools.append("google dorks")
    
    if virustotal_result != "":
        tools.append("virustotal")
    
    if shodan_result != "":
        tools.append("shodan")
    
    if searchsploit_result != "":
        tools.append("searchsploit")

    if whois_result != "":
        tools.append("whois")

    if ldap_result != "":
        tools.append("ldap")

    if mssql_result != "":
        tools.append("mssql")

    if mysql_result != "":
        tools.append("mysql")

    if wpscan_result != "":
        tools.append("wpscan")

    tools_used = ""
    for index in range (len(tools)):
        tools_used += tools[index]
        if index + 2 == len(tools):
            tools_used += ", and "
        elif index + 1 == len(tools):
            pass
        else:
            tools_used += ", "

    return tools_used

def input_timeout(input_display):
    try:
        # Take timed input using inputimeout() function
        data = inputimeout(prompt=input_display, timeout=60)

    # Catch the timeout error
    except Exception:
        # Declare the timeout statement
        data = "default"
    
    return data

def elapsed_time(start_time, end_time):
    total_time = end_time - start_time

    if (total_time > 3600):
        hours = int(total_time / 3600)
        minutes = int((total_time % 3600) / 60)
        seconds = int((total_time % 3660) % 60)
        print(f"Completed in {hours} hour(s), {minutes} minute(s) and {seconds} second(s)\n")
    elif (total_time > 60):
        minutes = int((total_time % 3600) / 60)
        seconds = int((total_time % 3660) % 60)
        print(f"Completed in {minutes} minute(s) and {seconds} second(s)\n")
    else:
        seconds = int((total_time % 3660) % 60)
        print(f"Completed in {seconds} second(s)\n")
    
    exit()