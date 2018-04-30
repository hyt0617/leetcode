# !/usr/bin/env python
# -*-coding: utf-8 -*-


def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = abs(n)
        x = 1 / x
    return x * myPow(x * x, int(n/2)) if n % 2 else myPow(x * x, int(n/2))


print(myPow(2.0, 10))