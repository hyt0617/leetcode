# !/usr/bin/env python
# -*-coding: utf-8 -*-
from listNode import ListNode


def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = pre.next.next
        pre.next, a.next, b.next = b, b.next, a
        pre = a
    return self.next
