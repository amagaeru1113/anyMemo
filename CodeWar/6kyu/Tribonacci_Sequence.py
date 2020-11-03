# https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    if n < 4:
        return signature[:n]

    for i in range(len(signature), n):
        signature.append(signature[i - 3] + signature[i - 2] + signature[i - 1])

    return signature
