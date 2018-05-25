# !/usr/bin/env python
# -*-coding: utf-8 -*-


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or (l2 and l2.val < l1.val):
        l1, l2 = l2, l1
    head = l1
    while head:
        if l2 and head.val <= l2.val:
            if (head.next and head.next.val >= l2.val) or not head.next:
                tmp = l2.next
                l2.next = head.next
                head.next = l2
                l2 = tmp
        head = head.next
    return l1