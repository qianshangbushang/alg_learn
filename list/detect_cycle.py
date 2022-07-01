# Definition for singly-linked list.

# 2(x + y) = x + n(y + z)  + y
# x = n (y + z) - y


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while slow != fast and fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next

        x = head
        while x != slow:
            x = x.next
            slow = slow.next

        return x
