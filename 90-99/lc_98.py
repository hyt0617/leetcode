# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    cur, stack, res = root, [], []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if not res:
            res.append(cur.val)
        else:
            is_max = res[-1] < cur.val
            if not is_max:
                return False
            else:
                res.append(cur.val)
        cur = cur.right
    return True
