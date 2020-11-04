# https://www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{}:{}:{}".format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))

