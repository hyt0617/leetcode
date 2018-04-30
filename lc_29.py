# !/usr/bin/env python
# -*-coding: utf-8 -*-


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    pos = (dividend > 0) is (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)

    count = 0
    while dividend >= divisor:
        tmp, i = dividend, 1
        while dividend >= tmp:
            dividend -= tmp
            count += i
            i <<= 1
            tmp <<= 1
    count = count if pos else 0-count
    return min(max(-2147483648, count), 2147483647)
