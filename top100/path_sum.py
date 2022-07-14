#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :path_sum.py
# @Time      :2022/7/14 11:11


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = -1000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def _trace(node: TreeNode):
            if not node:
                return 0

            left = max(0, _trace(node.left))
            right = max(0, _trace(node.right))
            self.result = max(self.result, left + right + node.val)
            return max(left, right) + node.val

        return self.result
