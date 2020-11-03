# https://www.codewars.com/kata/55c45be3b2079eccff00010f

import re


def order(sentence):
    if len(sentence) < 1:
        return ""

    regex = re.compile("\d+")
    d = {}

    for s in sentence.split():
        match = regex.findall(s)[0]
        d[match] = s

    _sorted = sorted(d.items(), key=lambda x: x[0])
    return " ".join([i[1] for i in _sorted])

