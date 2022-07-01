# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        return self._sum_(root, 0)

    def _sum_(self, node: TreeNode, x):
        new_x = x * 10 + node.val
        if not node.left and not node.right:
            return new_x
        new_sum = 0
        if node.left:
            new_sum += self._sum_(node.left, new_x)
        if node.right:
            new_sum += self._sum_(node.right, new_x)

        return new_sum
