# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

import collections


def duplicate_count(text):
    text = text.lower()
    if len(text) < 1:
        return 0

    c = collections.Counter(list(text))
    cm = c.most_common()
    if cm[0][1] == 1 and cm[1][1] == 1:
        return 0

    t = [i for i in cm if i[1] > 1]
    return len(t)
