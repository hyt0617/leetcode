# !/usr/bin/env python
# -*-coding: utf-8 -*-


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    cache = {}
    for i in nums:
        if i in cache:
            cache.pop(i)
        else:
            cache[i] = None
    return list(cache.keys())
