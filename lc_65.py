# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    try:
        tmp = float(s)
        return True
    except Exception as e:
        return False
