#!/usr/bin/env python3

import sys
import json
import animelist

if len(sys.argv) != 3:
    print("usage: getvecs.py [usersfile] [vecsfile]")
    exit(0)

with open(sys.argv[1]) as f:
    users = []
    for line in f:
        users.append(line.strip())
    
with open(sys.argv[1], "w") as f:
    for user in users[5:]:
        f.write(user + '\n')

users = users[:5]

with open(sys.argv[2]) as f:
    d = json.load(f)

with open(sys.argv[2], "w+") as f:
    for user in users:
        if user not in d:
            d[user] = animelist.userToVec(user)
    json.dump(d, f)

print("total users collected: " + str(len(d)))

