#!/usr/bin/env python3
"""Specialized data structure to make sure the search runs in linear time"""
import types

class rankings():
    """Sorted fixed-size array"""

    def __init__(self, size):
        self._len = size
        self._lst = list()

    def insert(self, item, value):
        high = len(self._lst)
        if (len(self._lst) != 0
                and self._lst[0].value < value): #edge case
            high = 0
        low = 0
        while high > low + 1:
            guess = (int) ((high + low) / 2)
            if self._lst[guess].value < value:
                high = guess
            else:
                low = guess
        self._lst.insert(high,
            types.SimpleNamespace(
                item=item,
                value=value
            )
        )

        if len(self._lst) > self._len:
            del self._lst[-1]

    def getList(self):
        return list(x.item for x in self._lst)

if __name__ == "__main__":
    from random import randint
    r = rankings(10)
    lst = list()
    for i in range(30):
        val = randint(1, 25)
        lst.append(val)

    print("unsorted list")
    print(lst)
    print()
    print("rankings")
    for x in lst:
        r.insert(chr(x + ord('a')), x)
    print(r.getList())

    print()
    print("sanity check")
    lst.sort(reverse=True)
    print(lst)
