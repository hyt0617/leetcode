# !/usr/bin/env python
# -*-coding: utf-8 -*-


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(nums, t, index, result, results):
        if t < 0:
            return
        if t == 0:
            results.append(result)
            return
        else:
            for i in range(index, len(nums)):
                if i != 0 and nums[i-1] == nums[i]:
                    continue
                if nums[index] > t:
                    break
                dfs(nums[i+1:], t - nums[i], index, result + [nums[i]], results)

    candidates.sort()
    res = []
    dfs(candidates, target, 0, [], res)
    return res


# combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
combinationSum2([2,5,2,1,2], 5)