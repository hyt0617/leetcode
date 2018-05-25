# !/usr/bin/env python
# -*-coding: utf-8 -*-


def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    is_cycle = False
    start = head
    end = head
    while start and end:
        start = start.next
        if not end.next:
            return None
        end = end.next.next
        if start == end:
            is_cycle = True
            break
    if not is_cycle:
        return None
    temp = head
    while temp != end:
        temp = temp.next
        end = end.next
    return temp
