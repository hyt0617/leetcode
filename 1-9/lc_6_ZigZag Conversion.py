# !/usr/bin/env python
# -*-coding: utf-8 -*-


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows > len(s):
        return s
    res = [''] * numRows
    index, step = 0, 1
    for c in s:
        res[index] += c
        if not index:
            step = 1
        if index == numRows - 1:
            step = -1
        index += step
    return ''.join(res)
