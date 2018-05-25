# !/usr/bin/env python
# -*-coding: utf-8 -*-
from listNode import ListNode


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    less = ListNode(-1)
    eg = ListNode(-1)
    pivot = head
    less_pivot = less
    eg_pivot = eg
    while pivot:
        if pivot.val < x:
            less_pivot.next = pivot
            less_pivot = less_pivot.next
        if pivot.val >= x:
            eg_pivot.next = pivot
            eg_pivot = eg_pivot.next
        pivot = pivot.next
    eg_pivot.next = None
    less_pivot.next = eg.next
    return less.next
