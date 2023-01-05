import basic_command

def enumeration(target, current_time, is_verbose):
    output_file = f"mssql_{target}.txt"
    output_directory = f"./result/{current_time}/"
    output = f"{output_directory}{output_file}"

    basic_command.mkdir(output_directory)

    basic_command.run_command(f"nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p1433 {target} -oN {output}")

    result = basic_command.read_file(f"{output}")

    return f"{result}"