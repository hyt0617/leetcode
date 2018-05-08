# !/usr/bin/env python
# -*-coding: utf-8 -*-
from listNode import ListNode


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    pivot = dummy
    carry = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        carry, val = divmod(v1 + v2 + carry, 10)
        pivot.next = ListNode(val)
        pivot = pivot.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry:
        pivot.next = ListNode(carry)
    return dummy.next
