#!/usr/bin/env python3
"""
This module interfaces with MyAnimeList.net
"""

import re
import requests
import json
import pprint
import sys
import time

def getTitle(id, sleeptime = 0):
    """Converts an anime ID to the corresponding title."""
    time.sleep(sleeptime)
    s = requests.get("https://myanimelist.net/anime/" + str(id)).text
    p_title = r'<span itemprop="name">(.*)</span'
    try:
        return re.findall(p_title, s)[0]
    except IndexError:
        return getTitle(id, sleeptime + 1)

def getJson(html):
    """Extracts the user data JSON from an MyAnimeList profile page in HTML."""
    p_json = r'data-items="([^"]*)">'
    return json.loads(re.findall(p_json, html)[0].replace(r'&quot;', '"'))

def makeVec(json):
    """Parsing some user data JSON into the corresponding vector"""
    scores = dict()
    for anime in json:
        score = anime['score']
        if score != 0:
            scores[anime['anime_id']] = score
    return scores

def userToVec(username):
    """Converts some username to the corresponding vector"""
    try:
        s = requests.get("https://myanimelist.net/animelist/" + username + "?status=7").text
        return makeVec(getJson(s))
    except Exception:
        print("Can't extract username: " + username)
        return dict()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 animelist.py username")
        exit(0)
    pp = pprint.PrettyPrinter(indent=4)
    vec = userToVec(sys.argv[1])
    pp.pprint(vec)
