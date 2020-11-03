# https://www.codewars.com/kata/55f2b110f61eb01779000053


def get_sum(a, b):
    if a == b:
        return a

    if a > b:
        s, e = b, a
    else:
        s, e = a, b

    return sum([i for i in range(s, e + 1)])

