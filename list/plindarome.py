# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mid = self.findMidNode(head)

        mid = self.reverse(mid)
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True

    def findMidNode(self, head):
        dummy = ListNode(-1, head)
        f, s = dummy, dummy
        while f:
            s = s.next
            f = f.next
            if f:
                f = f.next
            else:
                s = s.next
                break
        return s

    def reverse(self, node):
        root = None
        while node:
            tmp = node.next
            node.next = root
            root = node
            node = tmp
        return root
