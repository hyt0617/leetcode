# !/usr/bin/env python
# -*-coding: utf-8 -*-
from listNode import ListNode


def reverseBetween(head, m, n):
    if not head:
        return head
    dummy = ListNode(-1)
    dummy.next = head

    m_prev = dummy
    for i in range(m-1):
        m_prev = m_prev.next

    m_cur = m_prev.next
    rev_head = m_cur
    for i in range(n-m):
        next_ele = m_cur.next
        next_link = next_ele.next
        next_ele.next = rev_head
        rev_head = next_ele
        m_cur.next = next_link

    m_prev.next = rev_head
    return dummy.next
