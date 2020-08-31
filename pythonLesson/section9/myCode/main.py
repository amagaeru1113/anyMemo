import string

from Roboter.template import (
    what_your_name,
    which_restaurant_is_your_favorite,
    say_goodbye,
    roboter_favorite,
    ref_thx,
)
from Roboter.exportCSV import input_restaurant_count

csv_name = "restaurant_count.csv"

print(what_your_name)
# your_name = str(input())


def cleanList(restaurans):
    restaurans = [i for i in restaurans if len(i) > 4]  # 空の店名の物は除外
    di = {}
    for i in restaurans:
        splited = i[:-1].split(",")
        di[splited[0]] = int(splited[1])
    return di


with open(csv_name, "r") as f:
    # print(f.read())
    restaurans = f.readlines()[1:]
    restaurans = cleanList(restaurans)
    restaurans_sorted = sorted(restaurans.items(), key=lambda x: x[0])
    print(restaurans)

    for name in restaurans:
        # print(name, count)
        t = string.Template(roboter_favorite)
        contents = t.substitute(restaurant=name)
        print(contents)
        yesNo = str(input()).lower()


print(ref_thx)


# t = string.Template(which_restaurant_is_your_favorite)
# contents = t.substitute(name=your_name)
# print(contents)

# favorite_restaurant = str(input()).split()
# favorite_restaurant = " ".join([s.capitalize() for s in favorite_restaurant])
# print(favorite_restaurant)

# input_restaurant_count(favorite_restaurant, csv_name)


# t = string.Template(say_goodbye)
# contents = t.substitute(name=your_name, restaurant=favorite_restaurant)
# print(contents)

