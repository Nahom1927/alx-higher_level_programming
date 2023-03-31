#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()

    deco = ["utf8 content", content.decode()]
    headers = [["type", type(content)], ["content", content], deco]
    print("Body response:")
    for el in headers:
        print("\t- {}: {}".format(el[0], el[1]))
