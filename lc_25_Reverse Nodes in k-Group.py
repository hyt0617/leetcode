# !/usr/bin/env python
# -*-coding: utf-8 -*-


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    tmp = head
    my_queue = []
    my_order = []
    while tmp:
        for i in range(0, k):
            if tmp:
                my_queue.append(tmp)
                tmp = tmp.next
        if my_queue and len(my_queue) == k:
            my_order = my_queue + my_order
            del my_queue[:]
    tail = my_queue[0] if my_queue else None
    for ele in my_order:
        ele.next = tail
        tail = ele
    return tail
