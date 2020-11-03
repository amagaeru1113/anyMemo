# https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence):
    sentences = sentence.split(" ")

    if len(sentences) < 2:
        res = sentences[0] if len(sentences[0]) < 5 else sentences[0][::-1]
        return res

    for idx, t in enumerate(sentences):
        if len(t) >= 5:
            sentences[idx] = t[::-1]

    res = " ".join(sentences)

    return res
