# !/usr/bin/env python
# -*-coding: utf-8 -*-


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    nums.append(target)
    nums.sort()
    return nums.index(target)
