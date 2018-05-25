# !/usr/bin/env python
# -*-coding: utf-8 -*-


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [1]
    for _ in range(rowIndex):
        res = []
        for x, y in zip([0] + res, res + [0]):
            res.append(x + y)
    return res
