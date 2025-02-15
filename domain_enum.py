from subbrute import subbrute
import argparse
import validators
import hashlib
import requests
from rich.console import Console
from rich.table import Table

console = Console()

# TODO: Add argument for "-np" [no-ping] to stop http requests to server.
parser = argparse.ArgumentParser(description = 'Enumeration tool for finding and requesting HTML response.')
parser.add_argument('domain', help = 'Domain which you wish to scan.')
parser.add_argument('-a', '--all', help = 'Display all information, no-ping by default.', action = 'store_true')
parser.add_argument('-t', '--timeout', help = 'Time for subdomain to respond (seconds), default is 5')

def convertToValidInteger(value):
    if value is None:
        return 5

    if not value.isdigit():
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)

    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)

    return ivalue

def getSubdomainTable(domain):
    foundDomains = []

    for d in subbrute.run(domain):
        # Verbose, display all actions, skip rest.
        if args.all:
            print(d)
            continue

        record = {
            "domain": d[0],
            "type": d[1],
            "value": d[2]
        }

        if record['domain'] in foundDomains:
            continue

        if record['type'] != 'CNAME' and record['type'] != 'A':
            continue

        foundDomains.append(record['domain'])

        # TODO: Dynamic address schemas (http:// https://)
        try:
            response = requests.get(f'http://{record['domain']}', timeout=args.timeout)
            checksum = hashlib.md5(response.text.encode('utf-8')).hexdigest()
            testedDomain = record['domain']
            status = response.status_code

            responseLength = len(response.text)

            console.print(f'[bold yellow][Hit][/bold yellow] {checksum} - {testedDomain} - {status} - Response Length: {responseLength}')
        except:
            pass

def main(args):
    console.print('[bold green][Begin][/bold green] Subdomain enumeration starting.')

    args.timeout = convertToValidInteger(args.timeout)
    validators.domain(args.domain)
    getSubdomainTable(args.domain)

    console.print('[bold green][Success][/bold green] Subdomain enumeration complete.')

args = parser.parse_args()

if __name__ == '__main__':
    main(args)
