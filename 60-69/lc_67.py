# !/usr/bin/env python
# -*-coding: utf-8 -*-


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = ""
    if len(a) <= len(b):
        a, b = b, a
    left_length = len(a) - len(b)
    if left_length:
        b = "0" * left_length + b
    carry = 0
    i = len(a) - 1
    while i >= 0:
        carry, digit = divmod(int(a[i]) + int(b[i]) + carry, 2)
        res = str(digit) + res
        i -= 1
    if carry:
        res = str(carry) + res
    else:
        res = a[0: i+1] + res
    return res


print(addBinary("1010", "1011"))