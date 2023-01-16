import basic_command
from mailmerge import MailMerge

import nmap

def auto_report(host, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    tools_used, current_date, total_services, services = parsing_summary(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

    os_host = nmap.parsing_data(nmap_result)

    nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result = empty_check(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

    result_filename = write_to_docx(host, os_host, current_date, tools_used, total_services, services, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

    convert_docx_to_pdf(result_filename)

def write_to_docx(host, os_host, current_date, tools_used, total_services, services, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    template = "template_report.docx"
    result_filename = f"{host} Reconnaissance Report - {current_date}.docx"
    document = MailMerge(template)

    document.merge(
        host_docx = host,
        os_host_docx = os_host,
        current_date_docx = current_date,
        version_docx = basic_command.get_data_from_env("document_version"),
        company_name_docx = basic_command.get_data_from_env("company"),
        tools_used_docx = tools_used,
        total_services_docx = total_services,
        services_docx = services,

        nmap_docx = nmap_result,
        dig_docx = dig_result,
        dnsenum_docx = dnsenum_result,
        gdorks_docx = gdorks_result,
        virustotal_docx = virustotal_result,
        shodan_docx = shodan_result,
        searchsploit_docx = searchsploit_result,
        whois_docx = whois_result,
        ftp_docx = ftp_result,
        ssh_docx = ssh_result,
        whatweb_docx = whatweb_result,
        gobuster_dir_docx = directory_result,
        dirsearch_docx = dirsearch_result,
        gobuster_subdomain_docx = subdomain_result,
        nikto_docx = nikto_result,
        wpscan_docx = wpscan_result,
        wafw00f_docx = wafw00f_result,
        pop_docx = pop_result,
        enum4linux_docx = enum4linux_result,
        netbios_docx = netbios_result,
        ldap_docx = ldap_result,
        mssql_docx = mssql_result,
        mysql_docx = mysql_result
    )
    document.write(result_filename)

    return result_filename

def parsing_summary(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    tools_used = basic_command.get_tools_used(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)
    current_date = basic_command.current_date()
    total_services = str(len(open_ports))
    services = ""

    for open_port in open_ports:
        port = open_port.split("/")[0]
        service = open_port.split(" ")[3].lower()

        services += f"{service} in port {port},"
    
    services.rstrip(",")

    return tools_used, current_date, total_services, services
    
def empty_check(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    if nmap_result == "":
        nmap_result = "Service is not detected"

    if dig_result == "":
        dig_result = "Service is not detected"

    if dnsenum_result == "":
        dnsenum_result = "Service is not detected"

    if gdorks_result == "":
        gdorks_result = "Service is not detected"

    if virustotal_result == "":
        virustotal_result = "Service is not detected"

    if shodan_result == "":
        shodan_result = "Service is not detected"

    if searchsploit_result == "":
        searchsploit_result = "Service is not detected"

    if whois_result == "":
        whois_result = "Service is not detected"

    if ftp_result == "":
        ftp_result = "Service is not detected"

    if ssh_result == "":
        ssh_result = "Service is not detected"

    if dirsearch_result == "":
        dirsearch_result = "Service is not detected"

    if directory_result == "":
        directory_result = "Service is not detected"

    if subdomain_result == "":
        subdomain_result = "Service is not detected"

    if nikto_result == "":
        nikto_result = "Service is not detected"

    if wafw00f_result == "":
        wafw00f_result = "Service is not detected"

    if whatweb_result == "":
        whatweb_result = "Service is not detected"

    if pop_result == "":
        pop_result = "Service is not detected"

    if enum4linux_result == "":
        enum4linux_result = "Service is not detected"

    if netbios_result == "":
        netbios_result = "Service is not detected"

    if ldap_result == "":
        ldap_result = "Service is not detected"

    if mssql_result == "":
        mssql_result = "Service is not detected"

    if mysql_result == "":
        mysql_result = "Service is not detected"

    if wpscan_result == "":
        wpscan_result = "Service is not detected"

    return nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, shodan_result, searchsploit_result, whois_result, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, wafw00f_result, whatweb_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result

def convert_docx_to_pdf(result_filename):
    pdf_filename = result_filename.rstrip(".docx") + ".pdf"

    basic_command.run_command(f"abiword {result_filename} -t pdf -o {pdf_filename}")