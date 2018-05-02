# !/usr/bin/env python
# -*-coding: utf-8 -*-


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    head = 0
    tail = len(nums) - 1
    i = 0
    while i <= tail:
        if nums[i] == 2:
            nums[i], nums[tail] = nums[tail], nums[i]
            tail -= 1
            i -= 1
        elif nums[i] == 0:
            nums[head], nums[i] = nums[i], nums[head]
            head += 1
        i += 1
    print(nums)

print(sortColors([1,0,2,1,1,0]))
print(sortColors([2,0,2,1,1,0]))