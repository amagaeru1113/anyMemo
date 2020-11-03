# https://www.codewars.com/kata/550f22f4d758534c1100025a


def dirReduc(arr):
    dir = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    move = []

    for d in arr:
        if move and dir[d] == move[-1]:
            move.pop()
        else:
            move.append(d)

    return move
