# https://www.codewars.com/kata/5270d0d18625160ada0000e4


def score(dice):
    a1, b1 = divmod(dice.count(1), 3)
    a2 = dice.count(2) // 3
    a3 = dice.count(3) // 3
    a4 = dice.count(4) // 3
    a5, b5 = divmod(dice.count(5), 3)
    a6 = dice.count(6) // 3

    res = (
        a1 * 1000
        + b1 * 100
        + a5 * 500
        + b5 * 50
        + a2 * 200
        + a3 * 300
        + a4 * 400
        + a6 * 600
    )
    return res