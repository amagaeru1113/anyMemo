# https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def find_outlier(integers):
    l = ["even" if i % 2 == 0 else "odd" for i in integers]
    tmp = [i for i in l if l.count(i) == 1][0]
    return integers[l.index(tmp)]
