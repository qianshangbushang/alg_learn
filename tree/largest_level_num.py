# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.level = []

    def largestValues(self, root: TreeNode) -> List[int]:
        self.find_max([root])
        return self.level

    def find_max(self, node_list):
        next_level = []
        cur_max = None
        for node in node_list:  # type: TreeNode
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not cur_max or cur_max < node.val:
                cur_max = node.val
        self.level.append(cur_max)
        return self.find_max(next_level)


class Solution:

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            result.append(queue[0].val)
            for _ in range(0, len(queue)):
                x = queue.pop(0)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                if x.val > result[-1]:
                    result[-1] = x.val
        return result
