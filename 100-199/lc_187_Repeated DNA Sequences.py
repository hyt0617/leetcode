# !/usr/bin/env python
# -*-coding: utf-8 -*-


def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    seen = set()
    repeat = set()
    i = 0
    while i + 10 <= len(s):
        ss = s[i:i + 10]
        if ss in seen:
            repeat.add(ss)
        seen.add(ss)
        i += 1
    return list(repeat)
