from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.build_tree(1, n + 1)

    def build_tree(self, start, end) -> List[TreeNode]:
        if start == end:
            return [None]
        if start == end - 1:
            return [TreeNode(start)]

        result = []
        for x in range(start + 1, end):
            left = self.build_tree(start, x)
            right = self.build_tree(x + 1, end)

            pair = [(m, n) for m in left for n in right]
            for p in pair:
                root = TreeNode(x)
                root.left = p[0]
                root.right = p[1]
                result.append(root)
        return result
