# !/usr/bin/env python
# -*-coding: utf-8 -*-


def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    r = 0
    for c in s:
        r *= 26
        r += ord(c) - 64
    return r
