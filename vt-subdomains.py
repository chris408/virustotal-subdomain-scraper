#!/usr/bin/env python3
import requests
from os import environ
import os
import sys
import json

def main(domain, apikey):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':apikey,'domain':domain}
    try:
        response = requests.get(url, params=params)
        jdata = response.json()
        domains = sorted(jdata['subdomains'])
    except(KeyError):
        print("No domains found for %s" % domain)
        exit(0)
    except(requests.ConnectionError):
        print("Could not connect to www.virustotal.com", file=sys.stderr)
        exit(1)

    for domain in domains:
        print(domain)

if __name__ == '__main__':
    if len(sys.argv) != 2:
    	print("Usage: python3 vt-subdomains.py domain.com", file=sys.stderr)
    	sys.exit(1) 
    domain = sys.argv[1]
    if environ.get('VTAPIKEY'):
        apikey = os.environ['VTAPIKEY']
    else:
        print("VTAPIKEY environment variable not set. Quitting.", file=sys.stderr)
        sys.exit(1)
    main(domain, apikey)
