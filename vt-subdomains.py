import requests
from os import environ
import os
import sys
import json

def main(domain, apikey):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':apikey,'domain':domain}
    response = requests.get(url, params=params)
    jdata = response.json()
    domains = sorted(jdata['subdomains'])

    for domain in domains:
        print(domain)

if __name__ == '__main__':
    if len(sys.argv) != 2:
    	print("Usage: python3 vt-subdomains.py domain.com")
    	sys.exit(1) 
    domain = sys.argv[1]
    if environ.get('VTAPIKEY'):
        apikey = os.environ['VTAPIKEY']
    else:
        print("VTAPIKEY environment variable not set. Quitting.")
        sys.exit(1)
    main(domain, apikey)
