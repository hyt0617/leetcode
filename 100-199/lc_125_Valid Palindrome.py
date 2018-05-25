# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isPalindrome(s=""):
    c = s.lower()
    p = [a for a in c if a.isalnum()]
    return p == p[::-1]
