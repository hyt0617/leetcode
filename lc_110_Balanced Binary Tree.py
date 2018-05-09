# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def count_level(node):
        if not node:
            return 0
        cur = node
        q = [cur]
        start = 0
        next_nodes = len(q)
        level = 0
        while start < next_nodes:
            for i in range(start, next_nodes):
                n = q[i]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level += 1
            start, next_nodes = next_nodes, len(q)
        return level

    if not root:
        return True
    left, right = root.left, root.right
    q = [left, right]
    start = 0
    next_nodes = len(q)
    while start < next_nodes:
        for i in range(start, next_nodes, 2):
            left = q[i]
            right = q[i + 1]
            left_level = count_level(left)
            right_level = count_level(right)
            if not abs(left_level - right_level) <= 1:
                return False
            if left:
                q.append(left.left)
                q.append(left.right)
            if right:
                q.append(right.left)
                q.append(right.right)
        start, next_nodes = next_nodes, len(q)
    return True


def isBalanced_bottom_up(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        print('l:', left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1


def isBalanced_top_down(root):
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1
    if not root:
        return True
    left = height(root.left)
    right = height(root.right)
    return abs(left - right) <= 1 and isBalanced_top_down(root.left) and isBalanced_top_down(root.right)