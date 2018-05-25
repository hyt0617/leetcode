# !/usr/bin/env python
# -*-coding: utf-8 -*-


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        s = int(str(x)[::-1])
    else:
        s = -1 * int(str(-x)[::-1])
    return s if (-2) ** 31 < s < 2 ** 31 else 0
