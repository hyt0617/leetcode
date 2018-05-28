# !/usr/bin/env python
# -*-coding: utf-8 -*-


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []
    max_left = [0] * len(nums)
    max_right = [0] * len(nums)
    slide_max = []
    for i in range(len(nums)):
        if i % k == 0:
            max_left[i] = nums[i]
        else:
            max_left[i] = max(nums[i], max_left[i - 1])
    for i in range(len(nums) - 1, -1, -1):
        if i % k == k - 1:
            max_right[i] = nums[i]
        else:
            if i + 1 <= len(nums) - 1:
                max_right[i] = max(nums[i], max_right[i + 1])
            else:
                max_right[i] = nums[i]
    i = 0
    while i + k <= len(nums):
        slide_max.append(max(max_right[i], max_left[i + k - 1]))
        i += 1
    return slide_max
