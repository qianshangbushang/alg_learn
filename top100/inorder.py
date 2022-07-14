#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :inorder.py
# @Time      :2022/7/14 10:47


from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def _trace(node: TreeNode):
            if not node:
                return

            _trace(node.left)
            result.append(node.val)
            _trace(node.right)
            return
        _trace(root)
        return result
