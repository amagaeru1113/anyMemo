# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python


def dashatize(num):

    n = [i for i in str(num) if i != "-"]

    if "".join(n).isnumeric() and len(n) >= 2:
        res_l = create_response(n)
        return "".join(res_l)
    else:
        return n[0] if len(n) == 1 else "None"


def insert_hihun(k, v, length):
    if k == 0:
        return [v, "-"]
    elif k == length - 1:
        return ["-", v]
    else:
        return ["-", v, "-"]


def create_response(n):
    length = len(n)
    l = []
    drop_l = []
    tmp_n = -1

    for k, v in enumerate(n):
        if int(v) % 2 != 0:
            l.extend(insert_hihun(k, v, length))
        else:
            l.append(v)
    return "".join(l).replace("--", "-")

