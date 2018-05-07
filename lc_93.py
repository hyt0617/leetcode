# !/usr/bin/env python
# -*-coding: utf-8 -*-


def restoreIpAddresses(s):
    stack, res = [(0, 1, [])], []
    while stack:
        i, j, q = stack.pop(0)
        if i == len(s) and len(q) == 4: res.append(".".join(q))
        while len(q) < 4 and j <= len(s) and int(s[i:j]) < 256 and (s[i] != "0" or s[i:j] == "0"):
            _, j = stack.append((j, j + 1, q + [s[i:j]])), j + 1
    return res


print(restoreIpAddresses("010010"))
print(restoreIpAddresses("25525511135"))
