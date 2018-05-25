# !/usr/bin/env python
# -*-coding: utf-8 -*-


def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root:
        return
    left = root.left
    right = root.right
    root.left = None
    flatten(left)
    flatten(right)

    root.right = left
    cur = root
    while cur.right:
        cur = cur.right
    cur.right = right
