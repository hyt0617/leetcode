# !/usr/bin/env python
# -*-coding: utf-8 -*-


def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    for x in nums:
        y = x - 1
        while y in nums:
            y = y+1
        best = max(best, y-x)
    return best
