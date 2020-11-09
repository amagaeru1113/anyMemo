# https://www.codewars.com/kata/55c6126177c9441a570000cc


def order_weight(strng):
    strings = sorted(strng.split())
    res = sorted(strings, key=_sum_strings)
    return " ".join(res)


def _sum_strings(x):
    return sum([int(i) for i in x])
