# !/usr/bin/env python
# -*-coding: utf-8 -*-


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    i = 0
    j = i + 1
    while nums and j < len(nums):
        while nums[i] == nums[j]:
            j += 1
            if j == len(nums):
                break
        del nums[i:j - 1]
        i += 1
        j = i + 1
    return len(nums)
