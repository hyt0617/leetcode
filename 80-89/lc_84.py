# !/usr/bin/env python
# -*-coding: utf-8 -*-


def largestRectangleArea(heights):
    my_stack = []
    i = 0
    max_area = 0
    while i <= len(heights):
        h = 0 if i == len(heights) else heights[i]
        if not my_stack or h >= heights[my_stack[-1]]:
            my_stack.append(i)
        else:
            pivot = my_stack.pop()
            count = i if not my_stack else i - 1 - my_stack[-1]
            max_area = max(max_area, count * heights[pivot])
            i -= 1
        i += 1
    return max_area
