#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    values = {'email': argv[2]}
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        page = page.decode('utf-8')
    print(page)
