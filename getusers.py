#!/usr/bin/env python3

import requests
import re
import sys

if len(sys.argv) != 2:
    print("usage: getusers logfile")
    exit(0)

def getUsers():
    s = requests.get("https://myanimelist.net/users.php").text
    p_title = r'<a href="/profile/(?:.*)">((?:-|\w)+)</a>'
    return re.findall(p_title, s)

users = getUsers()
with open(sys.argv[1], "a") as logfile:
    for user in users:
        logfile.write(user + "\n")
