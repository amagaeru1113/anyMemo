# https://www.codewars.com/kata/56747fd5cb988479af000028

import math


def get_middle(s):
    t = math.floor(len(s) / 2)
    return s[t] if len(s) % 2 != 0 else s[t - 1 : t + 1]

