# !/usr/bin/env python
# -*-coding: utf-8 -*-


def nextPermutation(nums):
    """ nums: List[int], :rtype: in-place instead."""
    i = k = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i > 0:
        j = i - 1
        n = i
        while n < k and nums[n+1] > nums[j]:
            n += 1
        nums[n], nums[j] = nums[j], nums[n]
    m = i
    while m < k:
        nums[m], nums[k] = nums[k], nums[m]
        m += 1
        k -= 1
    print(nums)

#nextPermutation([1, 2, 3])
#nextPermutation([1, 3, 2])
#nextPermutation([2, 1, 3])
#nextPermutation([2, 3, 1])
#nextPermutation([3, 2, 1])
nextPermutation([1, 5, 1])
