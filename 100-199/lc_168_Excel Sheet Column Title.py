# !/usr/bin/env python
# -*-coding: utf-8 -*-


def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    alphabet = dict((i - 65 + 1, chr(i)) for i in range(65, 91))
    if n in alphabet:
        return alphabet[n]
    else:
        res = ""
        while n > 26:
            q, r = divmod(n, 26)
            if r == 0:
                q = q - 1
                r = 26
            res = alphabet[r] + res
            n = q
        if n:
            res = alphabet[n] + res
        return res
