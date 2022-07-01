"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            if node.val > node.next.val > insertVal:
                break
            if insertVal > node.val > node.next.val:
                break
            node = node.next
        node.next = Node(insertVal, node.next)
        return head
