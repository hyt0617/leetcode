# !/usr/bin/env python
# -*-coding: utf-8 -*-


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    res = [1, 2]
    if n < 3:
        return res[n - 1]
    if n >= 3:
        for i in range(2, n):
            res.append(res[i - 2] + res[i - 1])
    return res[-1]
