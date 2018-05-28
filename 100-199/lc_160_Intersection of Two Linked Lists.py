# !/usr/bin/env python
# -*-coding: utf-8 -*-


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return None
    sa = headA
    sb = headB
    while sa != sb:
        sa = headB if not sa else sa.next
        sb = headA if not sb else sb.next
    return sb
