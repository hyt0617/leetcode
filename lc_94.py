# !/usr/bin/env python
# -*-coding: utf-8 -*-


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if root and root.left:
        res += inorderTraversal(root.left)
    if root:
        res.append(root.val)
    if root and root.right:
        res += inorderTraversal(root.right)
    return res


def inorderTraversal_iteratively(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack, res = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
