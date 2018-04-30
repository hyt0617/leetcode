# !/usr/bin/env python
# -*-coding: utf-8 -*-


def fourSum(nums, target):
    nums.sort()

    def findNsum(nums, target, count, result, final):
        if len(nums) < count or count < 2 or target < nums[0] * count or target > nums[-1] * count:
            return
        if count == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    final.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                if s < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - count + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    findNsum(nums[i+1:], target - nums[i], count-1, result + [nums[i]], final)
        return

    r = []
    final = []
    findNsum(nums, target, 4, r, final)
    return final


