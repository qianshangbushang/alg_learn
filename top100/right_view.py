#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :right_view.py
# @Time      :2022/7/14 10:50


from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView())
