# !/usr/bin/env python
# -*-coding: utf-8 -*-
from treeNode import TreeNode


def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """

    def build(io, po):
        if not po:
            return None
        else:
            root_val = po[-1]
            root = TreeNode(root_val)
            root_idx = io.index(root_val)
            ltn = io[0:root_idx]
            rtn = io[root_idx + 1:]
            right_po = po[-1 - 1:-1 - (len(rtn)) - 1:-1][::-1]
            left_po = po[-1 - (len(rtn)) - 1::-1][::-1]

            root.left = build(ltn, left_po)
            root.right = build(rtn, right_po)
            return root

    return build(inorder, postorder)
