import re
import requests
import json
import pprint

def getTitle(id):
    s = requests.get("https://myanimelist.net/anime/" + str(id)).text
    p_title = r'<span itemprop="name">(.*)</span'
    return re.findall(p_title, s)[0]

def getJson(html):
    p_json = r'data-items="([^"]*)">'
    return json.loads(re.findall(p_json, html)[0].replace(r'\/', '/').replace(r'&quot;', '"'))

def makeVec(json):
    scores = dict()
    for anime in json:
        score = anime['score']
        if score != 0:
            scores['anime_id'] = score
    # TODO normalize and make z-scores
    
    return scores

#TODO rewrite me
def userToVec(username):
    try:
        s = requests.get("https://myanimelist.net/animelist/" + username + "?status=7").text
    except Exception:
        print("Dead link: " + username)
        return dict()
    rows = list()
    index = 0
    while True:
        index = s.find("<tr", index)
        if index == -1:
            break
        startRow = s.find(">", index) + 1
        endRow = s.find("</tr", startRow)
        rows.append(s[startRow: endRow])
        index = endRow

    print(s)

    #TODO this is placeholder
    # return {"PH_1": randint(1, 10), "PH_2": randint(1, 10)}
if __name__ == "__main__":
    with open("out.html") as f:
        s = f.read()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(getJson(s))

# print(getTitle(28819))
# print(getTitle(36456))
