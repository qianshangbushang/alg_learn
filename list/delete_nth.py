# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast, last = head, dummy
        while n > 0:
            fast = fast.next
            n = n - 1

        while fast:
            fast = fast.next
            last = last.next

        last.next = last.next.next
        return head
