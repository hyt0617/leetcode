# !/usr/bin/env python
# -*-coding: utf-8 -*-
from treeNode import TreeNode


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def build(nums):
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            root_val = nums[mid]
            root = TreeNode(root_val)
            ltn = nums[0:mid]
            rtn = nums[mid + 1:]
            root.left = build(ltn)
            root.right = build(rtn)
            return root

    return build(nums)
