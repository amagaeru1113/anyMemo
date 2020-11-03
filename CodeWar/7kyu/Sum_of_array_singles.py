# https://www.codewars.com/kata/59f11118a5e129e591000134


import collections


def repeats(arr):
    c = collections.Counter(arr)

    sum = 0
    for i in c.most_common():
        if i[1] == 1:
            sum += i[0]

    return sum
