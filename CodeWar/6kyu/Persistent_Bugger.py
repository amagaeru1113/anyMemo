# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

import numpy as np


def persistence(n):
    if n < 10:
        return 0

    mul = _prod(n)
    count = 0
    while True:
        count += 1
        if int(mul) < 10:
            break
        mul = _prod(mul)

    return count


def _prod(n):
    l_np = np.array([int(i) for i in str(n)])
    return np.prod(l_np)
