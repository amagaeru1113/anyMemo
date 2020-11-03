# https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string):
    return "".join([i for i in string if i.lower() not in ["a", "i", "u", "e", "o"]])

