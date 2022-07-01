# Definition for a binary tree node.
import re


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root