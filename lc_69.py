# !/usr/bin/env python
# -*-coding: utf-8 -*-


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    l = 1
    h = x
    res = 0
    while l <= h:
        m = int(l + (h - l) / 2)
        if m <= int(x/m):
            res = m
            l = m + 1
        else:
            h = m - 1
    return res


print(mySqrt(4))
print(mySqrt(8))
