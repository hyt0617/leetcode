# !/usr/bin/env python
# -*-coding: utf-8 -*-


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    res = []
    i = len(digits) - 1
    carry = 0
    while i >= 0:
        if i == len(digits) - 1:
            q, r = divmod(digits[i] + 1 + carry, 10)
        else:
            q, r = divmod(digits[i] + carry, 10)
        carry = q
        res.insert(0, r)
        i -= 1
        if not carry:
            break
    if carry:
        res.insert(0, carry)
    else:
        res = digits[0:i+1] + res
    return res


print(plusOne([9, 9, 9, 9]))
print(plusOne([9, 8, 9]))
print(plusOne([1, 2, 4]))

