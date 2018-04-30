# !/usr/bin/env python
# -*-coding: utf-8 -*-


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    import itertools
    r = itertools.permutations(nums)
    return [list(ele) for ele in r]


print(permute([1, 2, 3]))