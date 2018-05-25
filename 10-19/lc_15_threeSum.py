# !/usr/bin/env python
# -*-coding: utf-8 -*-


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # prevent duplicate
            continue
        high, low = i + 1, len(nums) - 1
        while high < low:
            cur_sum = nums[i] + nums[high] + nums[low]
            if cur_sum > 0:
                low -= 1
            elif cur_sum < 0:
                high += 1
            else:
                res.append([nums[i], nums[high], nums[low]])
                while high < low and nums[high] == nums[high + 1]:
                    high += 1
                while low > high and nums[low] == nums[low - 1]:
                    low -= 1
                high += 1
                low -= 1
    return res



