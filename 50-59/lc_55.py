# !/usr/bin/env python
# -*-coding: utf-8 -*-


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    lastPos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0
