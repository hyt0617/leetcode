# !/usr/bin/env python
# -*-coding: utf-8 -*-


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    matrix = [[0] * m for i in range(n)]
    matrix[0][0] = 1
    for i in range(n):
        for j in range(m):
            if j > 0:
                matrix[i][j] += matrix[i][j - 1]
            if i > 0:
                matrix[i][j] += matrix[i - 1][j]
    return matrix[-1][-1]


print(uniquePaths(3, 2))
