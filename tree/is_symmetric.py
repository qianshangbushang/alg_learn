# Definition for a binary tree node.

from tkinter.messagebox import NO


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_syme(root.left, root.right)
    
    def is_syme(self, A: TreeNode, B:TreeNode) -> bool:
        if not A and not B:
            return True
        if A is None and B is not None:
            return False
        if A is not None and B is None:
            return False
        
        if A.val != B.val:
            return False
        return self.is_syme(A.left, B.right) and self.is_syme(A.right, B.left)
