# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1:
            return False
        if self.isMatched(t1, t2):
            return True
        return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
    
    def isMatched(self, t1:TreeNode, t2:TreeNode) -> bool:
        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        return self.isMatched(t1.left, t2.left) and self.isMatched(t1.right, t2.right)