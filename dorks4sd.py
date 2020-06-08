#!/usr/bin/env python3

import googlesearch
from urllib.parse import urlparse
from urllib.error import HTTPError
import argparse
import os.path

def print_banner():
    print("    _         _       _ _         _ ")
    print(" __| |___ _ _| |__ __| | | ___ __| |")
    print("/ _` / _ \ '_| / /(_-<_  _(_-</ _` |")
    print("\__,_\___/_| |_\_\/__/ |_|/__/\__,_|")
    print("                                    ")

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def prepare_query(domain, subdomains):
    query = f"site:*.{domain}"
    for subdomain in subdomains:
        query += f' -site:{subdomain}'
    return query

def print_info(msg):
    print(f"[*] {msg}")

def print_error(msg):
    print(f"[ERROR] {msg}")

def print_list(lst):
    for l in lst:
        print(l)

def read_list_to_file(filename):
    lst = []
    if os.path.isfile(filename):
        f = open(filename, 'r')
        for l in f:
            lst += [l.strip()]
        f.close()
    return lst

def write_list_to_file(filename, lst):
    f = open(filename, 'w')
    for l in lst:
        f.write(l + '\n')
    f.close()

def print_results(domain, subdomains):
    print("")
    print_info(f'Results for {domain}:')
    print_list(subdomains)

def google_request(query, nb_links, delay, user_agent):
    print_info('The following google dorks query will be executed :')
    print(query)
    subdomains = []
    try:
        for url in googlesearch.search(query, stop=nb_links, pause=delay, user_agent=user_agent):
            o = urlparse(url)
            subdomain = o.netloc
            if subdomain not in subdomains:
                subdomains += [subdomain]
    except HTTPError as e:
        if e.code == 429:
            print_error("We are blocked by Google, Too Many Requests (429)")
            print_error("You can wait a few minutes and have some coffee")
            print_error("You can also increase the 'delay' option and change your public ip")
        else:
            raise
    return subdomains

def dorks_4_subdomains(domain, input_file, output_file, max_requests, delay, nb_links):
    print_banner()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'
    subdomains = read_list_to_file(input_file) if input_file else []
    for i in range(max_requests):
        query = prepare_query(domain, subdomains)
        new_subdomains = google_request(query, nb_links, delay, user_agent)
        if len(new_subdomains) == 0:
            print_info("No results found.")
            print_results(domain, subdomains)
            exit(0)
        else:
            print_info('The following subdomains have been found :')
            print_list(new_subdomains)
        subdomains = remove_duplicates(subdomains + new_subdomains)
        if output_file:
            write_list_to_file(output_file, subdomains)
            print_info(f'The subdomains found have been written in {output_file}')
    print_results(domain, subdomains)

if __name__ == "__main__":
    description = "Tool used for discovering subdomains using Google dorks.\n\n" \
                  "examples : \n" \
                  "          ./dorks4sd microsoft.com\n" \
                  "          ./dorks4sd microsoft.com --output subdomains.txt\n" \
                  "          ./dorks4sd microsoft.com --input subdomains.txt --output subdomains.txt\n" \
                  "          ./dorks4sd microsoft.com --output subdomains.txt --max-requests 10 --delay 4.0\n"
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('domain', help='target domain')
    parser.add_argument('--input', help='file containing a list of already known subdomains (for exclusion)')
    parser.add_argument('--output', help='save the subdomains found in a file')
    parser.add_argument('--max-requests', help='Maximum number of google query dorks made (default is 5)', type=int, default=5)
    parser.add_argument('--delay', help='set the delay interval between two Google requests (default is 2.0 seconds)', type=float, default=2.0)
    parser.add_argument('--nb-links', help='for each google dorks request, nb-links is the number of results examined (default is 10)', type=int, default=10)
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()
    domain = args.domain
    input_file = args.input
    output_file = args.output
    max_requests = args.max_requests
    delay = args.delay
    nb_links = args.nb_links
    dorks_4_subdomains(domain, input_file, output_file, max_requests, delay, nb_links)
