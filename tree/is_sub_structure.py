# Definition for a binary tree node.
from tkinter.messagebox import NO


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None:
            return False
        
        return self.isSame(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


    def isSame(self, A:TreeNode, B:TreeNode) -> bool:
        if B is None :
            return True

        if A is None or A.val != B.val:
            return False
        
        is_left_ok = self.isSame(A.left, B.left)
        is_right_ok = self.isSame(A.right, B.right)
        return is_left_ok and is_right_ok