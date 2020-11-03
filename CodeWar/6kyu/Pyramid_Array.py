# https://www.codewars.com/kata/515f51d438015969f7000013


def pyramid(n):

    pyramid = []
    if n > 0:
        for i in range(n):
            pyramid.append([1 for j in range(i + 1)])

    return pyramid
