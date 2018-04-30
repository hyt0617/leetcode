# !/usr/bin/env python
# -*-coding: utf-8 -*-


def romanToInt(s):
    """
    :type s: str
    :rtype: int - 1~3999
    """
    mapping = {
        'I': 1,
        'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    for i in range(0, len(s)-1):
        if mapping[s[i]] < mapping[s[i+1]]:
            result -= mapping[s[i]]
        else:
            result += mapping[s[i]]
    return result + mapping[s[-1]]
