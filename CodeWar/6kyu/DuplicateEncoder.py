# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c


def duplicate_encode(word):
    word = word.lower()
    t = [word.count(i) for i in word]
    res = []
    for k, v in enumerate(word):
        if t[k] > 1:
            res.append(")")
        else:
            res.append("(")

    return "".join(res)

