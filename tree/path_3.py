# Definition for a binary tree node.
from ast import Return
from typing import List

from pip import main


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def FindPath(self, root: TreeNode, sum: int) -> int:
        # write code here
        return self.find_path(root, [], sum)

    def find_path(self, node: TreeNode, choice: List[int], target: int) -> int:
        if not node:
            return 0

        new_choice = [x + node.val for x in choice]
        new_choice.append(node.val)

        cur_valid = len([x for x in new_choice if x == target])
        left_valid = self.find_path(node.left, new_choice, target)
        right_valid = self.find_path(node.right, new_choice, target)

        return cur_valid + left_valid + right_valid
