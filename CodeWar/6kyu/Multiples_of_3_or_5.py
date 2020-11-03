# https://www.codewars.com/kata/514b92a657cdc65150000006


def solution(number):
    ls = []
    for i in range(number):
        if i > 0:
            if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
                ls.append(i)
    return sum(ls)
