# !/usr/bin/env python
# -*-coding: utf-8 -*-


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    q = [root]
    level = 0
    cur = 0
    nextl = len(q)
    while cur < nextl:
        nodes = q[cur:nextl]
        for n in nodes:
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        level += 1
        cur = nextl
        nextl = len(q)
    return level
