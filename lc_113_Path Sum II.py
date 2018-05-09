# !/usr/bin/env python
# -*-coding: utf-8 -*-


def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if (not root and sum) or (not root and not sum):
        return []
    q = [(-1, root)]
    res = []
    cur = 0
    nextl = len(q)
    results = []
    while cur < nextl:
        for i in range(cur, nextl):
            parent_idx, node = q[i]
            if parent_idx == -1:
                res.append(node.val)
            else:
                res.append(node.val + res[parent_idx])
            if node.left:
                q.append((i, node.left))
            if node.right:
                q.append((i, node.right))
            if not node.left and not node.right:
                if parent_idx == -1:
                    results.append((-1, node.val))
                else:
                    results.append((parent_idx, node.val + res[parent_idx]))
        cur, nextl = nextl, len(q)
    sum_list = [ele for ele in results if ele[1] == sum]
    final = []
    for ele in sum_list:
        temp = []
        parent_idx, temp_sum = ele
        while parent_idx != -1:
            parent_idx, parent_node = q[parent_idx]
            temp.insert(0, parent_node.val)
            temp_sum -= parent_node.val
        temp.append(temp_sum)
        final.append(temp)
    return final


def pathSum_clean(root, sum):
    import collections
    if not root:
        return []
    res = []
    q = collections.deque([(root, root.val, [root.val])])
    while q:
        r, v, ls = q.popleft()
        if not r.left and not r.right and v == sum:
            res.append(ls)
        if r.left:
            q.append((r.left, v + r.left.val, ls + [r.left.val]))
        if r.right:
            q.append((r.right, v + r.right.val, ls + [r.right.val]))
    return res
