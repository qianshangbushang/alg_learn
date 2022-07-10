#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :zigzag_order.py
# @Time      :2022/7/9 10:44


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        result = []
        while queue:
            arr = []
            for idx in range(len(queue)):
                curr_node = queue.pop()
                arr.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if len(result) % 2 == 0:
                result.append(arr)
            else:
                result.append(arr[::-1])
        return result
