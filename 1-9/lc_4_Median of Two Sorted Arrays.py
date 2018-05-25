# !/usr/bin/env python
# -*-coding: utf-8 -*-


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    all_nums = sorted(nums1 + nums2)
    middle, left = divmod(len(all_nums), 2)
    if left == 1:
        return all_nums[middle]
    else:
        return float(all_nums[middle] + all_nums[middle - 1]) / 2.0
