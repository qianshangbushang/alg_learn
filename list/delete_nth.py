# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """

        :param head:
        :param n:
        :return:
        """

        """
          1 -> 2 -> 3 -> 4 -> 5
          
        """
        dummy = ListNode(-1, head)
        last = dummy
        first = head

        while n > 0 and first:
            first = first.next
            n -= 1

        if n > 0:
            return dummy.next

        while first:
            first = first.next
            last = last.next

        last.next = last.next.next
        return dummy.next
