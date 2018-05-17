#!/usr/bin/env python3
"""
usage: ./getusers.py logfile.txt
Pulls usernames from MyAnimeList.net, and write them into logfile.txt.
"""
import requests
import re
import sys

def getUsers():
    """Retrieves the list of 20 most recently online users"""
    s = requests.get("https://myanimelist.net/users.php").text
    p_title = r'<a href="/profile/(?:.*)">((?:-|\w)+)</a>'
    return re.findall(p_title, s)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: ./getusers.py logfile.txt")
        exit(0)

    users = getUsers()
    with open(sys.argv[1], "a") as logfile:
        for user in users:
            logfile.write(user + "\n")
