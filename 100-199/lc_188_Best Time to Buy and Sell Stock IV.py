# !/usr/bin/env python
# -*-coding: utf-8 -*-


def maxProfit(k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices or not k:
        return 0
    if k > len(prices) // 2:
        return sum([x-y for x, y in zip(prices[1:], prices[:-1]) if x > y])
    profits = [0] * len(prices)
    for j in range(k):
        pre_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            pre_profit = max(pre_profit + profit, profits[i])
            profits[i] = max(pre_profit, profits[i-1])
    return profits[-1]
