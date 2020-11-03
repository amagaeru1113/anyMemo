# https://www.codewars.com/kata/59e66e48fc3c499ec5000103

import itertools


def solve(arr):

    p = itertools.product(*arr)
    res = set(list(p))

    return len(res)

