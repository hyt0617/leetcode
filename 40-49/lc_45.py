# !/usr/bin/env python
# -*-coding: utf-8 -*-


def jump(nums):
    if len(nums) < 2:
        return 0
    level = 0
    currentMax = 0
    i = 0
    nextMax = 0

    while currentMax - i + 1 > 0:
        level += 1
        while i <= currentMax:
            nextMax = max(nextMax, nums[i] + i)
            if nextMax >= len(nums) - 1:
                return level
            i += 1
        currentMax = nextMax
    return 0


print(jump([1,1,3,1,1]))
print(jump([1, 2]))
print(jump([2,3,0,1,4]))
print(jump([2,3,1,1,4]))
print(jump([1,2,1,1,4]))
print(jump([1]))


