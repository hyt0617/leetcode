# !/usr/bin/env python
# -*-coding: utf-8 -*-


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None
    ln_length = 0
    tail = head
    while tail and tail.next:
        ln_length += 1
        tail = tail.next
    ln_length += 1
    rotate_times = k % ln_length
    reserve = ln_length - rotate_times
    pivot_start = head
    while reserve > 1:
        pivot_start = pivot_start.next
        reserve -= 1
    tail.next = head
    head = pivot_start.next
    pivot_start.next = None
    return head
