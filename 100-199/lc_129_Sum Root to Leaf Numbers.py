# !/usr/bin/env python
# -*-coding: utf-8 -*-


class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        self.travel(root, [])
        return self.total

    def travel(self, node, result):
        if node:
            if not node.left and not node.right:
                result.append(str(node.val))
                val_str = "".join(result)
                print(val_str)
                self.total += int(val_str) if val_str else 0
            else:
                result.append(str(node.val))
                self.travel(node.left, result)
                self.travel(node.right, result)
            result.pop()
