# !/usr/bin/env python
# -*-coding: utf-8 -*-


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            # find start & end
            start = low
            end = high
            while end > mid and nums[end] != target:
                end -= 1
            while start < mid and nums[start] != target:
                start += 1
            return [start, end]

        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return [-1, -1]