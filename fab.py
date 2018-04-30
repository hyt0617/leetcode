# !/usr/bin/env python
# -*-coding: utf-8 -*-


def fab(x):
    res = [1, 1]
    if x < 2:
        return res[x-1]
    else:
        for i in range(2, x):
            res.append(res[i-1] + res[i-2])
    return res[-1]


print(fab(5))
print(fab(4))
print(fab(3))