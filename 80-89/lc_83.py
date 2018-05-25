# !/usr/bin/env python
# -*-coding: utf-8 -*-


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pivot = head
    while pivot:
        next_ele = pivot.next
        while next_ele and next_ele.val == pivot.val:
            next_ele = next_ele.next
        pivot.next = next_ele
        pivot = pivot.next
    return head
