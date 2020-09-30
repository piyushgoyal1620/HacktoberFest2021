from math import factorial
from collections import Counter
from fractions import gcd


def cyclick_count(c, n):
    aa = factorial(n)
    for a, b in Counter(c).items():
        aa //= (a**b)*factorial(b)
    return aa


def cyclick_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for g in cyclick_partitions(n-i, i):
            yield [i] + g


def solution(w, h, s):
    grido = 0
    for cpw in cyclick_partitions(w):
        for cph in cyclick_partitions(h):
            m = cyclick_count(cpw, w)*cyclick_count(cph, h)
            grido = grido+ m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))

    return str(grido//(factorial(w)*factorial(h)))
