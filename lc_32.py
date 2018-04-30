# !/usr/bin/env python
# -*-coding: utf-8 -*-


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    my_stack = [-1]
    max_length = -1
    for idx, ele in enumerate(s):
        if ele == '(':
            my_stack.append(idx)
        else:
            my_stack.pop()
            if len(my_stack) == 0:
                my_stack.append(idx)
            else:
                max_length = max(max_length, idx - my_stack[-1])
    return max_length if max_length >= 0 else 0


longestValidParentheses(")()()(()")
