# !/usr/bin/env python
# -*-coding: utf-8 -*-


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    length = 0
    tmp = head
    while tmp:
        length += 1
        tmp = tmp.next
    remove_index = length - n

    if remove_index == 0:
        return head.next
    else:
        tmp = head
        prev = None
        cur_idx = 0
        while tmp:
            if cur_idx == remove_index:
                prev.next = tmp.next
                break
            else:
                prev = tmp
                tmp = tmp.next
                cur_idx += 1
        return head
