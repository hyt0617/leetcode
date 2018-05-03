# !/usr/bin/env python
# -*-coding: utf-8 -*-


def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def combination(nums, r, count, res):
        if count == 0:
            temp_r = sorted(r[:])
            if temp_r not in res:
                res.append(temp_r)
            return
        else:
            i = 0
            while i < len(nums):
                r.append(nums[i])
                combination(nums[i+1:], r, count-1, res)
                r.pop()
                i += 1
    min_length = 0
    max_length = len(nums)
    if max_length == min_length:
        return [[]]
    res = [[], nums[:]]
    for i in range(1, max_length):
        combination(nums, [], i, res)
    return res

print(subsetsWithDup([1, 2, 2]))

