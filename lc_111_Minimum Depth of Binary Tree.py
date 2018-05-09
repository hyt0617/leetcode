# !/usr/bin/env python
# -*-coding: utf-8 -*-


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def nearest(node):
        if node and not node.left and not node.right:
            return True
        return False

    def travel(node):
        if not node:
            return 0
        q = [node]
        cur = 0
        nextl = len(q)
        level = 0
        while cur < nextl:
            for i in range(cur, nextl):
                n = q[i]
                if nearest(n):
                    return level + 1
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level += 1
            cur, nextl = nextl, len(q)
        return level

    return travel(root)
