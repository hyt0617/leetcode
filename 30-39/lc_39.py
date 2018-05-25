# !/usr/bin/env python
# -*-coding: utf-8 -*-


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(nums, target, index, path, results):
        if target < 0:
            return
        if target == 0:
            results.append(path)
            return
        else:
            for i in range(index, len(nums)):
                dfs(nums, target - nums[i], i, path+[nums[i]], results)
    res = []
    dfs(candidates, target, 0, [], res)
    return res

# combinationSum([2, 3, 6, 7], 7)
# combinationSum([2, 3, 5], 8)
# combinationSum([1, 2], 3)
# combinationSum([2, 3, 7], 18)
combinationSum([2, 3, 8], 18)
