# !/usr/bin/env python
# -*-coding: utf-8 -*-


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    try:
        start = head
        end = head.next
        while start != end:
            start = start.next
            end = end.next.next
        return True
    except:
        return False
