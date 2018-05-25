# !/usr/bin/env python
# -*-coding: utf-8 -*-


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    words = s.split(" ")
    words = [w for w in words if w]
    return len(words[-1]) if len(words) else 0
