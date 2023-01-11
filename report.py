import basic_command
from mailmerge import MailMerge

import dig, dirsearch, dnsenum, enum4linux, gobuster, nikto, nmap, google, searchsploit, shodan, virustotal, whois, wpscan
import ftp, ssh, pop, netbios, ldap, mssql, mysql

def auto_report(host, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    tools_used, current_date, total_services, services = parsing_summary(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

    os_host = nmap.parsing_data(nmap_result)

    write_to_docx(host, os_host, current_date, tools_used, total_services, services, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)

def write_to_docx(host, os_host, current_date, tools_used, total_services, services, nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    template = "template_report.docx"
    document = MailMerge(template)

    document.merge(
        host_docx = os_host,
        current_date_docx = current_date,
        version_docx = basic_command.get_data_from_env("document_version"),
        company_docx = basic_command.get_data_from_env("company"),
        tools_used_docx = tools_used,
        total_services_docx = total_services,
        services_docx = services,

        nmap_docx = nmap_result,
        dig_docx = dig_result,
        dnsenum_docx = dnsenum_result,
        gdorks_docx = gdorks_result,
        virustotal_docx = virustotal_result,
        # shodan_docx = shodan_result,
        ftp_docx = ftp_result,
        ssh_docx = ssh_result,
        gobuster_dir_docx = directory_result,
        dirsearch_docx = dirsearch_result,
        gobuster_subdomain_docx = subdomain_result,
        nikto_docx = nikto_result,
        wpsdcan_docx = wpscan_result,
        pop_docx = pop_result,
        enum4linux_docx = enum4linux_result,
        netbios_docx = netbios_result,
        ldap_docx = ldap_result,
        mssql_docx = mssql_result,
        mysql_docx = mysql_result
    )
    document.write(f"{host} Reconnaissance Report - {current_date}.docx")

def parsing_summary(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result):
    tools_used = basic_command.get_tools_used(nmap_result, dig_result, dnsenum_result, gdorks_result, virustotal_result, open_ports, ftp_result, ssh_result, dirsearch_result, directory_result, subdomain_result, nikto_result, pop_result, enum4linux_result, netbios_result, ldap_result, mssql_result, mysql_result, wpscan_result)
    current_date = basic_command.current_date()
    total_services = str(len(open_ports))
    services = ""

    for open_port in open_ports:
        port = open_port.split("/")[0]
        service = open_port.split(" ")[3].lower()

        services = f"{service} in port {port},"
    
    services.rstrip(",")

    return tools_used, current_date, total_services, services
    
    