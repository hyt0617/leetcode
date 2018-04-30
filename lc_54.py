# !/usr/bin/env python
# -*-coding: utf-8 -*-


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    rec = []
    while matrix:
        rec += matrix.pop(0)
        matrix = [list(ele) for ele in zip(*matrix)]
        matrix = [list(ele) for ele in reversed(matrix)]
    return rec


'''print(spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))'''

'''print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))'''

print(spiralOrder([
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ],
 [13, 14, 15, 16]
]))