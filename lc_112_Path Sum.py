# !/usr/bin/env python
# -*-coding: utf-8 -*-


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root and not sum:
        return False
    if not root and sum:
        return False
    q = [(-1, root)]
    res = []
    results = []
    cur = 0
    nextl = len(q)
    while cur < nextl:
        for i in range(cur, nextl):
            parent_idx, node = q[i]
            if parent_idx == -1:
                res.append(node.val)
            else:
                res.append(node.val + res[parent_idx])
            if node.left:
                q.append((i, node.left))
            if node.right:
                q.append((i, node.right))
            if not node.left and not node.right:
                if parent_idx == -1:
                    results.append(node.val)
                else:
                    results.append(node.val + res[parent_idx])
        cur, nextl = nextl, len(q)
    return sum in results
