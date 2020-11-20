# https://www.codewars.com/kata/554e4a2f232cdd87d9000038


def DNA_strand(dna):
    d = {"A": "T", "T": "A", "G": "C", "C": "G"}
    l = [d[i] for i in dna]
    return "".join(l)
