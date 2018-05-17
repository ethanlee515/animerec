#!/usr/bin/env python3

import sys
import random
from random import randint
from math import sqrt
import rankings
import json
import animelist
import numpy
import types

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("usage: animerec username [animeID]")
    exit(0)

predictID = sys.argv[2] if len(sys.argv) == 3 else None

def dot(v1, v2):
    s = 0
    for key in v1:
        if key in v2:
            s += v1[key] * v2[key]
    return s

def normalize(vec):
    if vec == {}:
        return
    ratings = list()
    for animeID in vec:
        ratings.append(vec[animeID])
    arr = numpy.asarray(ratings)
    mean = numpy.mean(arr)
    sdev = numpy.std(arr)
    for animeID in vec:
        if sdev == 0:
            vec[animeID] = 0
        else:
            vec[animeID] = (vec[animeID] - mean) / sdev
    return (mean, sdev)

x0 = animelist.userToVec(sys.argv[1])
if x0 == {}:
    print("Cannot find " + sys.argv[1] + " on MyAnimeList")
    exit(0)

x = dict()
for animeID in x0:
    x[str(animeID)] = x0[animeID]

if predictID is not None:
    if predictID in x:
        print("You've given it a rating of " + str(x[predictID]) + ". Now let's pretend you haven't watched it...")
        del x[predictID]

mean, sdev = normalize(x)

with open("vecs.json") as f:
    users = json.load(f)

for name in users:
    normalize(users[name])

# Retrieve 30 closest neighbors
similarUsers = rankings.rankings(30)

for name in users:
    if name == sys.argv[1]:
        continue
    v = users[name]
    similarUsers.insert(v, dot(v, x))

scores = dict()
for vec in similarUsers.getList():
    for animeID in vec:
        if animeID in scores:
            scores[animeID].value += vec[animeID]
            scores[animeID].count += 1
        else:
            scores[animeID] = types.SimpleNamespace(value=vec[animeID], count=1)

critical_popularity = 10

if predictID is not None:
    if predictID not in scores:
        print("No data available.")
        exit(0)
    score = scores[predictID]
    if score.count < critical_popularity:
        print("Unpopular series; take prediction with a grain of salt.")
    print("Predicted rating: " + str(round((mean + sdev * score.value / score.count),2)))
else:
    # store up to 40 potential recommendations
    bestAnimes = rankings.rankings(40)
    for animeID in scores:
        score = scores[animeID]
        if score.count >= critical_popularity:
            bestAnimes.insert(animeID, score.value / score.count)

    outputted = 0
    for animeID in bestAnimes.getList():
        if outputted >= 5:
            break
        if animeID in x:
            continue
        print("https://myanimelist.net/anime/" + animeID)
        print(animelist.getTitle(animeID))
        outputted += 1
