import basic_command
import shodan

# ! input is_verbose
# ! api key set to .env

def scan(search_query, api_key, current_time, is_verbose):
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',
        ('country', 5),
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 5 Countries',
    }

    output = f"shodan_{search_query}_{current_time}.txt"
    output_directory = f"./result/current_time/shodan/"

    basic_command.mkdir(output_directory)

    try:
        # Setup the api
        api = shodan.Shodan(api_key)

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = api.count(search_query, facets=FACETS)

        # Print the summary info from the facets
        for facet in result['facets']:
            print (FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print ('%s: %s' % (term['value'], term['count']))

            # Print an empty line between summary info
            print ('')

    except (Exception, e):
        print ('Error: %s' % e)
        exit(1)