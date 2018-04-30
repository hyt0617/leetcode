# !/usr/bin/env python
# -*-coding: utf-8 -*-


def closestThreeSum(nums, target):
    res = None
    temp = sorted(nums)
    closest = -1
    for idx, n in enumerate(temp):
        if idx > 0 and temp[idx] == temp[idx - 1]:
            continue
        left, right = idx + 1, len(temp) - 1
        while left < right:
            cur_sum = n + temp[left] + temp[right]
            dis = abs(cur_sum-target)
            if closest == -1 or dis < closest:
                closest = dis
                res = cur_sum
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                while left < right and temp[left] == temp[left + 1]:
                    left += 1
                while left < right and temp[right] == temp[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return res
