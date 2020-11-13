# https://www.codewars.com/kata/56a5d994ac971f1ac500003e


def longest_consec(strarr, k):
    if not len(strarr) or k > len(strarr) or k <= 0:
        return ""

    res_length = 0
    res_text = 0
    for i in range(0, len(strarr) + 1 - k):
        text = "".join(strarr[i : i + k])
        if res_length < len(text):
            res_length = len(text)
            res_text = text

    return res_text
