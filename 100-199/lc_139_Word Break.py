# !/usr/bin/env python
# -*-coding: utf-8 -*-


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    r = [False] * (len(s) + 1)
    r[0] = True
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if r[j] and s[j:i] in wordDict:
                r[i] = True
                break
    return r[-1]


print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))