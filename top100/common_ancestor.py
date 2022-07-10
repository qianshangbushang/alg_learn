#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :common_ancestor.py
# @Time      :2022/7/9 14:12


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traceback(node: TreeNode):
            if not node:
                return None
            left, right = None, None
            if node.left:
                left = traceback(node.left)
            if node.right:
                right = traceback(node.right)

            if left and right or (node == p) or (node == q):
                return node

            if left: return left
            if right: return right
            return None

        return traceback(root)
