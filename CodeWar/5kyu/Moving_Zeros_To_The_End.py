# https://www.codewars.com/kata/52597aa56021e91c93000cb0

# 解答
def move_zeros(array):
    if not array:
        return []
    l = [v for v in array if v == 0 and str(v) != "False"]
    w = [v for v in array if v != 0 or str(v) == "False"]
    return w + l


# シンプルな解答
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)

