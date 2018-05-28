# !/usr/bin/env python
# -*-coding: utf-8 -*-


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    traveled = set()
    for idx, num in enumerate(numbers):
        if num in traveled:
            continue
        other = numbers.index(target - num, idx + 1) if target - num in numbers else -1
        if other != -1:
            return [idx + 1, other + 1]
        else:
            traveled.add(num)
