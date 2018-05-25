# !/usr/bin/env python
# -*-coding: utf-8 -*-


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    for idx, ele in enumerate(nums2):
        nums1[m + idx] = ele
    nums1.sort()
