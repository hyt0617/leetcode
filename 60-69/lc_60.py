# !/usr/bin/env python
# -*-coding: utf-8 -*-


def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    import math
    nums = [ele for ele in range(1, n+1)]
    result = []
    k = k - 1
    while k > 0:
        q, r = k // math.factorial(n-1), k % math.factorial(n-1)
        result.append(nums[q])
        nums.pop(q)
        n = n - 1
        k = r
    result += nums
    return "".join(str(ele) for ele in result)


print(getPermutation(3, 2))
print(getPermutation(3, 6))
print(getPermutation(2, 2))
print(getPermutation(3, 1))
print(getPermutation(4, 9))
print(getPermutation(3, 3))

