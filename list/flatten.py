"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        x = head
        self._flatten(x)
        return head

    def _flatten(self, head) -> 'Node':
        x = head
        while x.next:
            if x.child is None:
                x = x.next
                continue

            tmp = x.next

            x.next = x.child
            child_last = self._flatten(x.child)
            child_last.next = tmp
            tmp.prev = child_last
            x = tmp
        return x
