#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tree_camera.py
# @Time      :2022/7/1 23:41


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0

        def travel(node: TreeNode):
            if not node:
                return 2

            left = travel(node.left)
            right = travel(node.right)

            if left == 0 or right == 0:
                global result
                result += 1
                return 1

            if left == 1 or right == 1:
                return 2

            return 0

        if not travel(root):
            result += 1

        return result
