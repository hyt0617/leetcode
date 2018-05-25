# !/usr/bin/env python
# -*-coding: utf-8 -*-


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0]) if m else 0
    matrix = [[0] * n for i in range(m)]
    matrix[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if j > 0:
                if i == 0:
                    matrix[i][j] = grid[i][j] + matrix[i][j-1]
                else:
                    matrix[i][j] = min(grid[i][j] + matrix[i][j - 1], grid[i][j] + matrix[i - 1][j])
            if i > 0:
                if j == 0:
                    matrix[i][j] = grid[i][j] + matrix[i - 1][j]
                else:
                    matrix[i][j] = min(grid[i][j] + matrix[i][j - 1], grid[i][j] + matrix[i - 1][j])
    return matrix[-1][-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
