class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        left_valid = self.pathSum(root.left, targetSum)
        right_valid = self.pathSum(root.right, targetSum)

        valid = self.find_target(root, targetSum)

        return valid + left_valid + right_valid

    def find_target(self, node: TreeNode, target):
        if not node:
            return 0

        valid = 0
        if node.val == target:
            valid = 1

        left_valid = self.find_target(node.left, target - node.val)
        right_valid = self.find_target(node.right, target - node.val)

        return valid + left_valid + right_valid
