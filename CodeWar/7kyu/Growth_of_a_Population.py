# https://www.codewars.com/kata/563b662a59afc2b5120000c6


def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 += p0 * percent * 0.01 + aug
        count += 1

    return count
