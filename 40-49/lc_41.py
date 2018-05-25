# !/usr/bin/env python
# -*-coding: utf-8 -*-


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    my_stack = []
    for i in range(0, len(nums) + 2):
        my_stack.append(i)
    for n in nums:
        if n <= 0:
            continue
        if n <= len(nums):
            my_stack[n] = 0
    res = 0
    for i in range(len(my_stack) - 1, -1, -1):
        if my_stack[i] != 0 and my_stack[i] != res:
            res = my_stack[i]
    return res


print(firstMissingPositive([2, 1]))
print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
