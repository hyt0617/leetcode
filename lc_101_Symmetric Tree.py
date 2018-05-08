# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def is_mirror(ln, rn):
        if not ln and not rn:
            return True
        if not ln or not rn:
            return False
        return (ln.val == rn.val) & is_mirror(ln.right, rn.left) & is_mirror(ln.left, rn.right)

    return is_mirror(root, root)
