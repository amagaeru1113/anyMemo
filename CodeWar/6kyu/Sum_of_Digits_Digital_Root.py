# https://www.codewars.com/kata/541c8630095125aba6000c00


def digital_sum(x):
    if x < 10:
        return x
    return x % 10 + digital_sum(x // 10)


def digital_root(n):
    if n < 10:
        return n
    return digital_root(digital_sum(n))
