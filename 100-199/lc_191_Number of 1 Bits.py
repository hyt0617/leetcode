# !/usr/bin/env python
# -*-coding: utf-8 -*-


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    b = '{:032b}'.format(n)
    bits = [bit for bit in b if bit == '1']
    return len(bits)
