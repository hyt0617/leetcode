# !/usr/bin/env python
# -*-coding: utf-8 -*-


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            return mid
        if (nums[low] <= target < nums[mid]) or (
                        nums[mid] < nums[high] and (target > nums[high] or target < nums[mid])):
            high = mid - 1
        else:
            low = mid + 1
    return -1

search([5, 1, 3], 3)
