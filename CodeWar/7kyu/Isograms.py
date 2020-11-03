# https://www.codewars.com/kata/54ba84be607a92aa900000f1


def is_isogram(string):
    string = string.lower()
    return len(string) == sum([string.count(i) for i in string])
