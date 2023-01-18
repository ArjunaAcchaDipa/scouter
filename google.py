import basic_command

def dorks(target, current_time, is_verbose):
    output_file = f"gdorks_{target}.txt"
    output_directory = f"./result/{target}/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)
    
    gdorks_result = (f""".git folders - https://www.google.com/search?q=inurl%3A%5C%22%2F.git%5C%22%20{target}%20-github
Backup files - https://www.google.com/search?q=site%3A{target}%20ext%3Abkf%20%7C%20ext%3Abkp%20%7C%20ext%3Abak%20%7C%20ext%3Aold%20%7C%20ext%3Abackup
Exposed documents - https://www.google.com/search?q=site%3A{target}%20ext%3Adoc%20%7C%20ext%3Adocx%20%7C%20ext%3Aodt%20%7C%20ext%3Apdf%20%7C%20ext%3Artf%20%7C%20ext%3Asxw%20%7C%20ext%3Apsw%20%7C%20ext%3Appt%20%7C%20ext%3Apptx%20%7C%20ext%3Apps%20%7C%20ext%3Acsv
Config files - https://www.google.com/search?q=site%3A{target}%20ext%3Axml%20%7C%20ext%3Aconf%20%7C%20ext%3Acnf%20%7C%20ext%3Areg%20%7C%20ext%3Ainf%20%7C%20ext%3Ardp%20%7C%20ext%3Acfg%20%7C%20ext%3Atxt%20%7C%20ext%3Aora%20%7C%20ext%3Aenv%20%7C%20ext%3Aini
Database files - https://www.google.com/search?q=site%3A{target}%20ext%3Asql%20%7C%20ext%3Adbf%20%7C%20ext%3Amdb
Other files - https://www.google.com/search?q=site%3A{target}%20intitle%3Aindex.of%20%7C%20ext%3Alog%20%7C%20ext%3Aphp%20intitle%3Aphpinfo%20%5C%22published%20by%20the%20PHP%20Group%5C%22%20%7C%20inurl%3Ashell%20%7C%20inurl%3Abackdoor%20%7C%20inurl%3Awso%20%7C%20inurl%3Acmd%20%7C%20shadow%20%7C%20passwd%20%7C%20boot.ini%20%7C%20inurl%3Abackdoor%20%7C%20inurl%3Areadme%20%7C%20inurl%3Alicense%20%7C%20inurl%3Ainstall%20%7C%20inurl%3Asetup%20%7C%20inurl%3Aconfig%20%7C%20inurl%3A%5C%22%2Fphpinfo.php%5C%22%20%7C%20inurl%3A%5C%22.htaccess%5C%22%20%7C%20ext%3Aswf
SQL errors - https://www.google.com/search?q=site%3A{target}%20intext%3A%5C%22sql%20syntax%20near%5C%22%20%7C%20intext%3A%5C%22syntax%20error%20has%20occurred%5C%22%20%7C%20intext%3A%5C%22incorrect%20syntax%20near%5C%22%20%7C%20intext%3A%5C%22unexpected%20end%20of%20SQL%20command%5C%22%20%7C%20intext%3A%5C%22Warning%3A%20mysql_connect- %5C%22%20%7C%20intext%3A%5C%22Warning%3A%20mysql_query- %5C%22%20%7C%20intext%3A%5C%22Warning%3A%20pg_connect- %5C%22
PHP errors - https://www.google.com/search?q=site%3A{target}%20%5C%22PHP%20Parse%20error%5C%22%20%7C%20%5C%22PHP%20Warning%5C%22%20%7C%20%5C%22PHP%20Error%5C%22
Wordpress files - https://www.google.com/search?q=site%3A{target}%20inurl%3Awp-content%20%7C%20inurl%3Awp-includes
Subdomains - https://www.google.com/search?q=site%3A*.{target}
Sub-subdomains - https://www.google.com/search?q=site%3A*.*.{target}
Login pages - https://www.google.com/search?q=site%3A{target}%20inurl%3Asignup%20%7C%20inurl%3Aregister%20%7C%20intitle%3ASignup
Open redirects - https://www.google.com/search?q=site%3A{target}%20inurl%3Aredir%20%7C%20inurl%3Aurl%20%7C%20inurl%3Aredirect%20%7C%20inurl%3Areturn%20%7C%20inurl%3Asrc%3Dhttp%20%7C%20inurl%3Ar%3Dhttp
Stackoverflow - https://www.google.com/search?q=site%3Astackoverflow.com%20%22{target}%22
Apache Struts RCE - https://www.google.com/search?q=site%3A{target}%20ext%3Aaction%20%7C%20ext%3Astruts%20%7C%20ext%3Ado
Linkedin employees - https://www.google.com/search?q=site%3Alinkedin.com%20employees%20{target}\n""")

    basic_command.run_command(f"echo \"{gdorks_result}\" {output}")

    if is_verbose:
        print("[+] Google Dorks\n")
        print(gdorks_result)

    return gdorks_result