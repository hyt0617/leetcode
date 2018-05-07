# !/usr/bin/env python
# -*-coding: utf-8 -*-


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    my_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    res = ""
    q, r = divmod(num, 1000)
    if q > 0:
        res += my_dict[1000] * q

    def generate(num, floor, mid, ceil):
        q, r = divmod(num, floor)
        s = ""
        if q < 4:
            s += my_dict[floor] * q
        elif q == 4:
            s += my_dict[floor] + my_dict[mid]
        elif q < 9:
            s += my_dict[mid] + (my_dict[floor] * (q - 5))
        elif q == 9:
            s += my_dict[floor] + my_dict[ceil]
        return r, s

    r, s = generate(r, 100, 500, 1000)
    res += s
    r, s = generate(r, 10, 50, 100)
    res += s
    r, s = generate(r, 1, 5, 10)
    res += s
    return res
