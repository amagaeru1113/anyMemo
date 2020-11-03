# https://www.codewars.com/kata/54c27a33fb7da0db0100040e

# 一回目
import math


def is_square(n):
    if n < 0:
        return False
    return math.sqrt(n).is_integer()


# 二回目
import math


def is_square(n):
    return False if n < 0 else math.sqrt(n).is_integer()
