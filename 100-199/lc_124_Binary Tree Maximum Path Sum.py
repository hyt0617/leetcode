# !/usr/bin/env python
# -*-coding: utf-8 -*-

import sys


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_value = -sys.maxsize - 1
        self.findMax(root)
        return self.max_value

    def findMax(self, node):
        if not node:
            return 0
        left = max(0, self.findMax(node.left))
        right = max(0, self.findMax(node.right))
        self.max_value = max(self.max_value, left + right + node.val)
        return max(left, right) + node.val
