# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _is_symmetric(node1: TreeNode, node2: TreeNode):
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            outer_ok = _is_symmetric(node1.left, node2.right)
            inner_ok = _is_symmetric(node1.right, node2.left)
            return outer_ok and inner_ok
        return _is_symmetric(root.left, root.right)
