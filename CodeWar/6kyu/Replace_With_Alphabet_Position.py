# https://www.codewars.com/kata/546f922b54af40e1e90001da

import string


def alphabet_position(text):
    alphabets = string.ascii_uppercase

    text = text.upper()
    text = [str(alphabets.index(t) + 1) for t in text if t.isalpha()]

    return " ".join(text) if len(text) > 0 else ""

