#!/usr/bin/env python3

import sys
import random
from random import randint
from math import sqrt
import rankings
import json
import animelist
import numpy

if len(sys.argv) != 3:
    print("usage: animerec username dataset")
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

sim = dot #TODO command line flag

x = animelist.userToVec(sys.argv[1])

if x == {}:
    print("cannot find " + sys.argv[1] + " on MyAnimeList")
    exit(0)

normalize(x)

with open(sys.argv[2]) as f:
    users = json.load(f)

for name in users:
    normalize(users[name])

similarUsers = rankings.rankings(10)

for name in users:
    if name == sys.argv[1]:
        continue
    v = users[name]
    similarUsers.insert(v, sim(v, x))

prediction = dict()
for vec in similarUsers.getList():
    for animeID in vec:
        if animeID in prediction:
            prediction[animeID] += vec[animeID]
        else:
            prediction[animeID] = vec[animeID]

bestAnimes = rankings.rankings(5)
for anime in prediction:
    bestAnimes.insert(anime, prediction[anime])

for i in bestAnimes.getList():
    print("https://myanimelist.net/anime/" + str(i))
    print(animelist.getTitle(i))


