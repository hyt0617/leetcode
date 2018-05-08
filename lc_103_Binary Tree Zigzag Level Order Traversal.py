# !/usr/bin/env python
# -*-coding: utf-8 -*-


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    q = [root]
    cur = 0
    reverse = False
    results = []
    nextl = len(q)
    while cur < nextl:
        temp_list = []
        nodes = q[cur:len(q)]
        for node in nodes:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            temp_list.append(node.val)
        if reverse:
            temp_list = temp_list[::-1]
        results.append(temp_list)
        reverse = bool(not reverse)
        cur = nextl
        nextl = len(q)
    return results
