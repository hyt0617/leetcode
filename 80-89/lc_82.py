# !/usr/bin/env python
# -*-coding: utf-8 -*-
from listNode import ListNode


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dmh = ListNode(-1)
    temp = dmh
    while head:
        if head.next and head.val == head.next.val:
            x = head.val
            while head and head.val == x:
                head = head.next
        else:
            temp.next = head
            head = head.next
            temp = temp.next
    temp.next = None
    return dmh.next
