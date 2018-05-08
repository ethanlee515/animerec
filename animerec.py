#!/usr/bin/env python3

import sys
import random
from random import randint
from math import sqrt
import rankings

if len(sys.argv) != 2:
    print("usage: animerec username")
    exit(0)

username = sys.argv[1]
try:
    uservec = animelist.userToVec(username)
except Exception:
    print("cannot find " + username + " on MyAnimeList")
    exit(0)

def dot(v1, v2):
    s = 0
    for key in v1:
        if key in v2:
            s += v1[key] * v2[key]
    return s

def cos_sim(v1, v2):
    d = dot(v1, v2)
    if d == 0:
        return 0
    return d / sqrt(dot(v1, v1) * dot(v2, v2))

sim = dot #TODO command line flag

users = dict() #TODO populate this

r = rankings.rankings(50)

for user in users:
    if user.name == username:
        continue
    r.insert(user.vec, sim(user.vec, uservec))

# now use r...
lst = r.getList()
for vec in lst:
    
    pass

"myanimelist.net/anime/36456"
