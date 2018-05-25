# !/usr/bin/env python
# -*-coding: utf-8 -*-


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    q = [root]
    result = []
    while len(q) > 0:
        temp_list = []
        temp_node_list = []
        for node in q:
            if node.left:
                temp_node_list.append(node.left)
            if node.right:
                temp_node_list.append(node.right)
            temp_list.append(node.val)
        result.append(temp_list)
        q = temp_node_list[:]
    return result
