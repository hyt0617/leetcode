# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    return int(str(abs(x))[::-1]) == x
