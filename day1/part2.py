"""
Advent of Code 2021 - Day 1

Using itertools because I like to overcomplicate things.
"""

from itertools import *
from operator import *


def sanitize(line):
    return int(line.rstrip("\n"))


def counter(pair):
    pv, nx = pair
    return 1 if nx > pv else 0


with open("input.dat") as file:
    lines = file.readlines()


sane = list(map(sanitize, lines))
windows = list(zip(sane[0:], sane[1:], sane[2:]))
collapsed = list(map(sum, windows))
pairs = zip(collapsed[0:], collapsed[1:])
result = accumulate(
    map(counter, pairs),
    func=add, initial=0
)


print(list(result)[-1])
