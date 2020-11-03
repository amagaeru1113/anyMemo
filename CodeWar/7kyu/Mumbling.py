# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039


def accum(s):

    strings = []
    for k, v in enumerate(s):
        tmp = "".join([v for i in range(k + 1)])
        strings.append(tmp.lower().capitalize())

    return "-".join(strings)

