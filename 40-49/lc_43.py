# !/usr/bin/env python
# -*-coding: utf-8 -*-


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    index = 0
    result = []
    for i in range(len(num2)-1, -1, -1):
        carry = 0
        temp_r = ""
        for j in range(len(num1)-1, i, -1):
            q, r = divmod(int(num1[j]) * int(num2[i]) + carry, 10)
            carry = q
            temp_r = str(r) + temp_r
        temp_r = str(carry) + temp_r
        result.append(int(temp_r) * (10**index))
        index += 1
    return str(sum(result))


# print(multiply("99", "9"))
# print(multiply("2", "3"))
print(multiply("123", "56"))
print(multiply("123", "456"))
