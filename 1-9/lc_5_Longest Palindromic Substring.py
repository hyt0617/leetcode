# !/usr/bin/env python
# -*-coding: utf-8 -*-


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    if len(s) < 2:
        return s

    def extend(ss, m, n, low, max_length):
        while m >= 0 and n < len(ss) and s[m] == s[n]:
            m -= 1
            n += 1
        if max_length < n-m-1:
            max_length = n-m-1
            low = m+1
        return low, max_length

    low = 0
    max_length = 0
    for i in range(len(s)):
        low, max_length = extend(s, i, i, low, max_length)
        low, max_length = extend(s, i, i+1, low, max_length)
    return s[low:low+max_length]


def longestPalindrome_clean(s):
    if not s:
        return s
    max_length = 1
    start = 0
    for i in range(len(s)):
        extend = i - max_length
        if extend >= 1 and s[extend-1:i+1] == s[extend-1:i+1][::-1]:
            start = extend - 1
            max_length += 2
            continue
        if extend >= 0 and s[extend:i+1] == s[extend:i+1][::-1]:
            start = extend
            max_length += 1
    return s[start:start+max_length]


print(longestPalindrome_clean("cbbd"))
print(longestPalindrome_clean("abb"))
print(longestPalindrome_clean("abab"))
print(longestPalindrome_clean("babad"))