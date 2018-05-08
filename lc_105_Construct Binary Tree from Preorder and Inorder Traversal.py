# !/usr/bin/env python
# -*-coding: utf-8 -*-
from treeNode import TreeNode


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    def build(preorder, inorder):
        if not preorder:
            return None
        else:
            root_val = preorder[0]
            root = TreeNode(root_val)
            root_val_idx = inorder.index(root_val)
            ltn = inorder[0:root_val_idx]
            rtn = inorder[root_val_idx + 1:]
            root.left = build(preorder[1:len(ltn) + 1], ltn)
            root.right = build(preorder[len(ltn) + 1:], rtn)
            return root

    return build(preorder, inorder)
