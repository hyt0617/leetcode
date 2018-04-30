# !/usr/bin/env python
# -*-coding: utf-8 -*-


def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    result = ""
    for idx, s in enumerate(zip(*strs)):
        if len(set(s)) == 1:
            result += s[0]
        else:
            return result
    return result
