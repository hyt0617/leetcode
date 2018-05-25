# !/usr/bin/env python
# -*-coding: utf-8 -*-


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_dict = {}
    for idx, ele in enumerate(nums):
        if target - ele in my_dict:
            return [my_dict[target - ele], idx]
        else:
            my_dict[ele] = idx
