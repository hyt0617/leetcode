# !/usr/bin/env python
# -*-coding: utf-8 -*-


def recoverTree(self, root):
    self.firstEle, self.secondEle, self.pre = None, None, None

    def travel(node):
        if not node:
            return
        travel(node.left)
        if self.pre and self.pre.val > node.val:
            if not self.firstEle:
                self.firstEle = self.pre
            self.secondEle = node
        self.pre = node
        travel(node.right)
    travel(root)
    self.firstEle.val, self.secondEle.val = self.secondEle.val, self.firstEle.val
