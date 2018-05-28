# !/usr/bin/env python
# -*-coding: utf-8 -*-

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    times = k % len(nums)
    while times:
        t = nums.pop()
        nums.insert(0, t)
        times -= 1


def rotate_1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:k], nums[k:] = nums[n - k:], nums[:n - k]