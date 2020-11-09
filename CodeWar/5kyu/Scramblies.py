# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

from collections import Counter


def scramble(s1, s2):
    c = Counter(s1)
    c.subtract(Counter(s2))
    return all(i >= 0 for i in c.values())
