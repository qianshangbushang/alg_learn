# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        root = None
        cnt = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val
            node = ListNode(val % 10 + cnt)
            node.next = root
            root = node
            cnt = val // 10
        return root

    def reverse(self, head: ListNode) -> ListNode:
        root = None

        while head:
            tmp = head.next
            head.next = root
            root = head
            head = tmp
        return root
