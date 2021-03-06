# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            first_match = i < len(s) and p[j] in {s[i], '?', '*'}
            if j < len(p) and p[j] == '*':
                dp[i][j] = dp[i][j + 1] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]
    return dp[0][0]


print(isMatch('aa', '*'))
