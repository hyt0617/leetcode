# !/usr/bin/env python
# -*-coding: utf-8 -*-


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """

    def bsearch(nums, target):
        h = 0
        t = len(nums) - 1
        while h <= t:
            m = (h + t) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                h = m + 1
            elif nums[m] > target:
                t = m - 1
        return False

    if not nums:
        return False
    head = 0
    tail = len(nums) - 1
    pivot = head
    while pivot < tail and nums[pivot + 1] >= nums[pivot]:
        pivot += 1
    if nums[head] == target or nums[pivot] == target or nums[tail] == target:
        return True
    if nums[head] < target < nums[pivot]:
        # find here
        return bsearch(nums[head:pivot + 1], target)
    elif pivot < tail and nums[pivot + 1] <= target < nums[tail]:
        # find here
        return bsearch(nums[pivot + 1:tail + 1], target)
    else:
        return False
