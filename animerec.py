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

if len(sys.argv) != 2:
    print("usage: animerec username")
    exit(0)

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

x0 = animelist.userToVec(sys.argv[1])
x = dict()
for animeID in x0:
    x[str(animeID)] = x0[animeID]

if x == {}:
    print("cannot find " + sys.argv[1] + " on MyAnimeList")
    exit(0)

normalize(x)

with open("vecs.json") as f:
    users = json.load(f)

for name in users:
    normalize(users[name])

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

bestAnimes = rankings.rankings(40)
for animeID in scores:
    score = scores[animeID]
    if score.count >= 10:
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
