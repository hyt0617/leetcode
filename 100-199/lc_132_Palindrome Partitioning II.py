# !/usr/bin/env python
# -*-coding: utf-8 -*-


def minCut(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = list(range(-1, n))
    for idx in range(1, n):
        for low, high in (idx, idx), (idx - 1, idx):
            while low >= 0 and high < n and s[low] == s[high]:
                dp[high + 1] = min(dp[high + 1], dp[low] + 1)
                low -= 1
                high += 1
    return dp[-1]


print(minCut("aab"))
