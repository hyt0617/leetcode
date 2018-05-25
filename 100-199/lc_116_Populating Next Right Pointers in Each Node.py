# !/usr/bin/env python
# -*-coding: utf-8 -*-


def connect(root):
    if root:
        nodes = [root.left, root.right]
        cur = 0
        nextl = len(nodes)
        while cur < nextl:
            tail = None
            for i in range(cur, nextl, 2):
                first = nodes[i]
                second = nodes[i + 1]
                if tail:
                    second.next = tail.next
                    tail.next = first
                if first and second:
                    first.next = second
                    tail = second
                if first and first.left and first.right:
                    nodes += [first.left, first.right]
                if second and second.left and second.right:
                    nodes += [second.left, second.right]
            cur, nextl = nextl, len(nodes)
