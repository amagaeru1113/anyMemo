# https://www.codewars.com/kata/54da5a58ea159efa38000836

import collections


def find_it(seq):
    c = collections.Counter(seq)
    count = c.most_common()
    res = None
    for i in count:
        if i[1] % 2 > 0:
            res = i[0]
    return res
