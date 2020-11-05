# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

import collections


def anagrams(word, words):
    res = [i for i in words if collections.Counter(word) == collections.Counter(i)]
    return res
