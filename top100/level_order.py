#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :level_order.py
# @Time      :2022/7/9 10:20


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        length = 1

        result = []
        while length > 0:
            arr = []
            while length > 0:
                x = queue.pop(0)
                arr.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                length -= 1
            length = len(queue)
            result.append(arr)
        return result
