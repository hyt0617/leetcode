# !/usr/bin/env python
# -*-coding: utf-8 -*-


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[-1]
    r = [0] * (len(nums) + 2)
    for i in range(len(nums)):
        r[i + 1] = nums[i]
        r[-1] = max(r[-1], r[i + 1])
    for i in range(3, len(nums) + 1):
        r[i] = max(r[i - 2], r[i - 3]) + r[i]
        r[-1] = max(r[-1], r[i])
    return r[-1]
