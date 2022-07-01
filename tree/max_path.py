class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#     5
#    4 8
# 11 N 13 4
# 7  2

class Solution:
    def __init__(self):
        self.max_sum = -1000

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.findSum(root)
        return self.max_sum

    def findSum(self, node: TreeNode):
        if not node:
            return 0
        right_sum = self.findSum(node.right)
        left_sum = self.findSum(node.left)

        cur_max = max(node.val, node.val + right_sum, node.val + left_sum)

        if cur_max > self.max_sum:
            self.max_sum = cur_max

        all_sum = node.val + right_sum + left_sum
        if all_sum > self.max_sum:
            self.max_sum = all_sum

        return cur_max
