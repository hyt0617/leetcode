# !/usr/bin/env python
# -*-coding: utf-8 -*-


def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    return 0 if n < 5 else int(n / 5 + self.trailingZeroes(n / 5))
