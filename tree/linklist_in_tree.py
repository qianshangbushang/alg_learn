from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isMatched(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isMatched(self, node: ListNode, root: TreeNode):
        if not node:
            return True

        if not root or node.val != root.val:
            return False

        return self.isMatched(node.next, root.left) or self.isMatched(node.next, root.right)
