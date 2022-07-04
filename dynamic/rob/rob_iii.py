#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rob_iii.py
# @Time      :2022/7/4 10:15


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        a: 抢不包含该节点的最大收益
        b: 抢包含该节点的最大收益

        :param root:
        :return:
        """
        if not root:
            return 0

        def travel(node: TreeNode):
            if not node:
                return 0, 0

            a_l, b_l = travel(node.left)
            a_r, b_r = travel(node.right)

            return b_l + b_r, max(node.val + a_l + a_r, b_l + b_r)

        a, b = travel(root)
        return max(a, b)
