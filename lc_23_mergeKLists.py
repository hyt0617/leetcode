# !/usr/bin/env python
# -*-coding: utf-8 -*-

from listNode import ListNode


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    import heapq
    my_queue = []
    for sll in lists:
        head = sll
        while head:
            heapq.heappush(my_queue, head.val)
            head = head.next
    my_queue.sort()
    if my_queue:
        head = ListNode(my_queue[0])
        cur = head
        for i in range(1, len(my_queue)):
            tmp = ListNode(my_queue[i])
            cur.next = tmp
            cur = tmp
        return head
