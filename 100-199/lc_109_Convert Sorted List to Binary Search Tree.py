# !/usr/bin/env python
# -*-coding: utf-8 -*-
from treeNode import TreeNode


def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if not head:
        return None
    cur = head
    nums = []
    while cur:
        nums.append(cur.val)
        cur = cur.next

    def build(nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root_val = nums[mid]
        root = TreeNode(root_val)
        ltn = nums[0:mid]
        rtn = nums[mid + 1:]
        root.left = build(ltn)
        root.right = build(rtn)
        return root

    return build(nums)
