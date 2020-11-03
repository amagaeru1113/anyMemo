# https://www.codewars.com/kata/54ff3102c1bad923760001f3

import collections


def get_count(input_str):
    if len(input_str) == 0:
        return 0

    list = [1 for y in input_str if y in ["a", "e", "i", "o", "u"]]
    return sum(list)
