# !/usr/bin/env python
# -*-coding: utf-8 -*-


def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle:
        return haystack.index(needle) if needle in haystack else -1
    return 0
