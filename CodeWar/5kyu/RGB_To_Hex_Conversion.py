# https://www.codewars.com/kata/513e08acc600c94f01000001


def rgb(r, g, b):
    html_color = "%02X%02X%02X" % (_check_rgb(r), _check_rgb(g), _check_rgb(b))
    return html_color


def _check_rgb(x):
    if x < 0:
        return 0
    if x > 255:
        return 255
    return x
