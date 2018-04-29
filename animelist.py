import re
import requests

def getTitle(id):
    s = requests.get("https://myanimelist.net/anime/" + str(id)).text
    p_title = r'<span itemprop="name">(.*)</span'
    return re.findall(p_title, s)[0]




# print(getTitle(28819))
# print(getTitle(36456))
