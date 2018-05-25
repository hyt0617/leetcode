# !/usr/bin/env python
# -*-coding: utf-8 -*-


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    stack = []
    if not prices:
        return 0
    start = 0
    profit = 0
    while start < len(prices):
        if not stack:
            stack.append(prices[start])
        else:
            if prices[start] < stack[-1]:
                stack.append(prices[start])
            else:
                profit = max(profit, prices[start] - stack[-1])
        start += 1
    return profit
