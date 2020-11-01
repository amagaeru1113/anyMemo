# https://www.codewars.com/kata/54da539698b8a2ad76000228

# 一回目
import collections


def is_valid_walk_1(walk):
    c = collections.Counter(walk)

    if sum(c.values()) == 10:
        if len(c.keys()) == 2:
            return True if _check("n", "s", c) or _check("w", "e", c) else False
        elif len(c.keys()) == 4:
            return True if c["n"] == c["s"] and c["w"] == c["e"] else False

        else:
            return False
    else:
        return False


def _check(s1, s2, c):
    return True if s1 in c.keys() and s2 in c.keys() and c[s1] == c[s2] else False


# 二回目
# 条件は移動の回数が10かつ東西の移動回数が等しくかつ南北の移動回数が等しい
# 一回目の要素の数での判別がいらなかった
def is_valid_walk_2(walk):
    w = True if len(walk) == 10 else False
    if w and walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e"):
        return True
    else:
        return False
