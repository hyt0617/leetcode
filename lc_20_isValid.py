# !/usr/bin/env python
# -*-coding: utf-8 -*-

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    match = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    my_stack = []
    for c in s:
        if my_stack:
            if c in match and my_stack[-1] == match[c]:
                my_stack.pop()
            else:
                my_stack.append(c)
        else:
            my_stack.append(c)
    return True if not my_stack else False
