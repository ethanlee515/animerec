import re
import requests
import json
import pprint
import sys

def getTitle(id):
    s = requests.get("https://myanimelist.net/anime/" + str(id)).text
    p_title = r'<span itemprop="name">(.*)</span'
    return re.findall(p_title, s)[0]

def getJson(html):
    p_json = r'data-items="([^"]*)">'
    return json.loads(re.findall(p_json, html)[0].replace(r'&quot;', '"'))

def makeVec(json):
    scores = dict()
    for anime in json:
        score = anime['score']
        if score != 0:
            scores[anime['anime_id']] = score
    return scores

def userToVec(username):
    try:
        s = requests.get("https://myanimelist.net/animelist/" + username + "?status=7").text
        return makeVec(getJson(s))
    except Exception:
        print("Can't extract: " + username)
        return dict()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 animelist.py username")
        exit(0)
    pp = pprint.PrettyPrinter(indent=4)
    vec = userToVec(sys.argv[1])
    pp.pprint(vec)

