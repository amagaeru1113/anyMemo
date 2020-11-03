# https://www.codewars.com/kata/5f70c55c40b1c90032847588

import collections


def set_list(es):
    return len(list(set(es))) == 1


def points(dice):
    dice = [d for d in dice]
    c = collections.Counter(dice)
    num_list = c.most_common()

    # GENERALA
    if len(c) == 1 and set_list(dice):
        return 50

    # POKER
    if len(c) == 2 and (num_list[0][1] == 4 or num_list[1][1] == 4):
        return 40

    # FULLHOUSE
    if len(c) == 2 and (num_list[0][1] == 3 or num_list[1][1] == 3):
        return 30

    # STRAIGHT
    straight_list = ["12345", "23456", "13456"]
    if len(c) >= 3:
        s_list = "".join(sorted(dice))
        if s_list in straight_list:
            return 20
        else:
            return 0

    return 0
