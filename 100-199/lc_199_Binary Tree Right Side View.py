# !/usr/bin/env python
# -*-coding: utf-8 -*-


def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    right_most = {}
    stack = [(root, 0)]
    depth = -1
    while stack:
        node, level = stack.pop()
        if node:
            depth = max(depth, level)
            right_most.setdefault(depth, node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
    return [right_most[depth] for depth in range(depth + 1)]
