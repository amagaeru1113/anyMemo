# https://www.codewars.com/kata/54e6533c92449cc251001667


def unique_in_order(iterable):

    if len(iterable) == 0:
        res = []
    elif len(iterable) == 1:
        res = [iterable]
    else:
        res = [
            iterable[i]
            for i in range(0, len(iterable) - 1)
            if iterable[i] != iterable[i + 1]
        ]
        res.append(iterable[-1])
    return res
