# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa.next else headB
            pb = pb.next if pb.next else headA
        return pa


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.cnt_len(headA)
        len_b = self.cnt_len(headB)

        if len_a > len_b:
            x = len_a
            while x > len_a:
                x -= 1
                headA = headA.next
        if len_b > len_a:
            x = len_b
            while x > len_b:
                x -= 1
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headB
            headB = headB.next
            headA = headA.next
        return None

    def cnt_len(self, head: ListNode):
        list_len = 0
        while head:
            head = head.next
            list_len += 1
        return list_len
