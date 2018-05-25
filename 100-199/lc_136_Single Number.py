# !/usr/bin/env python
# -*-coding: utf-8 -*-


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for num in nums:
        res ^= num
    return res
