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

#TODO rewrite me
def userToVec(username):
    #TODO this is placeholder
    return {"PH_1": randint(1, 10), "PH_2": randint(1, 10)}

def dot(v1, v2):
    s = 0
    for key in v1:
        if key in v2:
            s += v1[key] * v2[key]
    return s

def sim(v1, v2):
    d = dot(v1, v2)
    if d == 0:
        return 0
    return d / sqrt(dot(v1, v1) * dot(v2, v2))
