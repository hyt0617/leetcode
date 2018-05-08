# !/usr/bin/env python
# -*-coding: utf-8 -*-


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    q = [root]
    cur = 0
    nextl = len(q)
    results = []
    while cur < nextl:
        temp_list = []
        for i in range(cur, nextl):
            node = q[i]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            temp_list.append(node.val)
        results.insert(0, temp_list)
        cur, nextl = nextl, len(q)
    return results
