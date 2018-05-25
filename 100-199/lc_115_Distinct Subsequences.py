# !/usr/bin/env python
# -*-coding: utf-8 -*-


def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0] * (len(s) + 1) for _ in range((len(t) + 1))]
    for i in range(len(dp[0])):
        dp[0][i] = 1

    for i in range(len(t)):
        for j in range(len(s)):
            if s[j] == t[i]:
                dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
            else:
                dp[i+1][j+1] = dp[i+1][j]
    return dp[len(t)][len(s)]


print(numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("rabbbit", "rabbit"))

