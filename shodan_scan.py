import basic_command
import shodan

def scan(search_query, api_key, current_time, is_verbose):
    output_file = f"shodan_{search_query}.txt"
    output_directory = f"./result/{search_query}/{current_time}/"
    output = f"{output_directory}{output_file}"

    results = ""

    FACETS = [
        'org',
        'domain',
        'port',
        ('country', 5),
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'country': 'Top 5 Countries',
    }

    basic_command.mkdir(output_directory)

    api_key = default_check(api_key)

    if api_key.startswith("Skipping"):
        if is_verbose:
            print(f"[!] {api_key}\n")
        return api_key

    if is_verbose:
        print("[+] Running Shodan scan\n")

    try:
        # Setup the api
        api = shodan.Shodan(api_key)

        result = api.count(search_query, facets=FACETS)

        for facet in result['facets']:
            results += f"{FACET_TITLES[facet]}\n"

            for term in result['facets'][facet]:
                results += f"{term['value']}: {term['count']}\n"

            results += "\n"
        
        results = results.rstrip("\n")

        basic_command.run_command(f"echo '{results}' > {output}")

        if is_verbose:
            print(f"{results}\n")
        
        return results

    except Exception as e:
        print(f"Error:\n{e}")
        exit(1)
    
def default_check(api_key):
    if api_key == "":
        api_key = basic_command.input_timeout("\n[-] API Key for Shodan (timeout in 60 seconds): ")
        if api_key == "default" or api_key == "":
            api_key = "Skipping Shodan because there is no API Key inputted"
            print(f"[!] Shodan will be skipped because no API Key were inputted\n")
    
    return api_key