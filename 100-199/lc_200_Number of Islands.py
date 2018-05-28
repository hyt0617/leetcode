# !/usr/bin/env python
# -*-coding: utf-8 -*-


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def markz(territory, m, n):
        if m < 0 or n < 0 or m >= len(territory) or n >= len(territory[0]) or territory[m][n] != '1':
            return
        territory[m][n] = '0'
        markz(territory, m - 1, n)
        markz(territory, m, n - 1)
        markz(territory, m, n + 1)
        markz(territory, m + 1, n)

    if not grid:
        return 0
    if not grid[0]:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                markz(grid, i, j)
                count += 1
    return count
