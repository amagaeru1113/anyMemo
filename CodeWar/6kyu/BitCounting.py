# https://www.codewars.com/kata/526571aae218b8ee490006f4

# 一回目
def count_bits(n):
    return len([i for i in bin(n)[2:] if i == "1"])


# 良い回答
def count_bits(n):
    return bin(n).count("1")
