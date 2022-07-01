class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = False

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        right = self.inorderSuccessor(root.right, p)
        if right:
            return right
        if self.flag:
            return root
        if root.val == p.val:
            self.flag = True
        return None
