# !/usr/bin/env python
# -*-coding: utf-8 -*-


def connect(root):
    if not root:
        return root
    nodes = [root.left, root.right]
    cur = 0
    nextl = len(nodes)
    while cur < nextl:
        tail = None
        for i in range(cur, nextl):
            node = nodes[i]
            if not node:
                continue
            if tail:
                node.next = tail.next
                tail.next = node
                tail = node
            else:
                tail = node
            nodes += [node.left, node.right]
        cur, nextl = nextl, len(nodes)
