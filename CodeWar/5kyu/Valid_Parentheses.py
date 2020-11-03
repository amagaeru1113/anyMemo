# https://www.codewars.com/kata/52774a314c2333f0a7000688

# ペアを作って仲間外れを探す


def valid_parentheses(string):
    l = []

    for p in string:

        if p == ")":
            if not l:
                return False
            l.pop()
        elif p == "(":
            l.append(p)
        else:
            continue

    return not l
