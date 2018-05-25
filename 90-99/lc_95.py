# !/usr/bin/env python
# -*-coding: utf-8 -*-

from treeNode import TreeNode


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def gensub(nums):
        if not nums:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[-1])]
        nodeList = []
        for i in range(len(nums)):
            leftArr = gensub(nums[0:i])
            rightArr = gensub(nums[i + 1:])
            for l in leftArr:
                for r in rightArr:
                    node = TreeNode(nums[i])
                    node.left = l
                    node.right = r
                    nodeList.append(node)
        return nodeList
    if not n:
        return []
    nums = [i for i in range(1, n+1)]
    return gensub(nums)


print(generateTrees(3))
