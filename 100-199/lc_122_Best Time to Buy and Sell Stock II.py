# !/usr/bin/env python
# -*-coding: utf-8 -*-


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for i in range(0, len(prices) - 1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit


print(maxProfit([1,2,3,4,5]))
print(maxProfit([1,2,7,4]))
