# !/usr/bin/env python
# -*-coding: utf-8 -*-


def reverseBits(n):
    return int('{:032b}'.format(n)[::-1], 2)
