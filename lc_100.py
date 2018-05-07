# !/usr/bin/env python
# -*-coding: utf-8 -*-


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if (p and not q) or (not p and q):
        return False

    def travel(root):
        res, cur = [], root
        if cur:
            res.append(cur.val)
            if cur.left:
                res += travel(cur.left)
            else:
                res += [None]
            if cur.right:
                res += travel(cur.right)
            else:
                res += [None]
        return res

    p_val = travel(p)
    q_val = travel(q)
    print(len(p_val), len(q_val))
    if len(p_val) != len(q_val):
        return False

    for i in range(0, len(p_val)):
        if p_val[i] != q_val[i]:
            return False
    return True
