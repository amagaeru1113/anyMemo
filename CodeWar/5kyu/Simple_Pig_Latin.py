# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    res = [i[1:] + i[0] + 'ay' if i not in ['?', '!'] else i for i in text.split()]
    return ' '.join(res)s