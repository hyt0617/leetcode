# !/usr/bin/env python
# -*-coding: utf-8 -*-


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0]) if m else 0
    matrix = [[0] * n for i in range(m)]
    matrix[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                continue
            if j > 0:
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1] if obstacleGrid[i][j-1] == 0 else matrix[i][j] + 0
            if i > 0:
                matrix[i][j] = matrix[i][j] + matrix[i - 1][j] if obstacleGrid[i-1][j] == 0 else matrix[i][j] + 0
    return matrix[-1][-1]


print(uniquePathsWithObstacles([[1]]))
