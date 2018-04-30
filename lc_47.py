# !/usr/bin/env python
# -*-coding: utf-8 -*-


def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    import itertools
    r = itertools.permutations(nums)
    return set(r)


print(permuteUnique([1, 1, 2]))