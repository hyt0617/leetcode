# !/usr/bin/env python
# -*-coding: utf-8 -*-


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    result = [[1]]
    for i in range(2, numRows + 1):
        temp = []
        p = 0

        for j in range(i):
            if j == 0 or j == i - 1:
                temp.append(1)
            else:
                temp.append(result[i - 2][p] + result[i - 2][p + 1])
                p += 1
        result.append(temp[:])
    return result
