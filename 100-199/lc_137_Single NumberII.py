# !/usr/bin/env python
# -*-coding: utf-8 -*-


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def compute(nums, times):
        k = times - 1
        bits = [0] * k
        for num in nums:
            for i in range(k):
                mask = -1
                for j in range(k):
                    if j != i:
                        mask &= ~bits[j]
                bits[i] = (bits[i] ^ num) & mask
        return bits[0]

    return compute(nums, 3)


def singleNumber_1(nums):
    a = set(nums)
    v = sum(a) * 3 - sum(nums)
    return int(v/2)


print(singleNumber_1([2,2,3,2]))