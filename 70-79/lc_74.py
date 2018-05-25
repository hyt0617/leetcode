# !/usr/bin/env python
# -*-coding: utf-8 -*-


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    headers = [ele[0] for ele in matrix]
    if target in headers:
        return True
    else:
        low, high = 0, len(headers)
        mid = 0
        while low < high:
            mid = int((low + high) / 2)
            if headers[mid] > target > headers[mid-1]:
                break
            if headers[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        possible_row = mid - 1 if target < headers[mid] else mid
        return target in matrix[possible_row]


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))
