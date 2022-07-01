# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        mid = self.find_mid(head)

        new_tail = self.reverseList(mid)

        x = head
        while x:
            tmp = x.next
            x.next = new_tail
            new_tail = new_tail.next
            x = x.next
            x.next = tmp


    # s = 1        s = 2        s = 3
    # f = 1 f = 2  f = 3  f = 4 f = 5
    def find_mid(self, head: ListNode):
        dummy = ListNode(-1, head)
        s, f = dummy, dummy
        while f:
            s = s.next
            f = f.next
            if not f:
                return s
            f = f.next
        return s

    def reverseList(self, head: ListNode):
        new_head = None

        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = []

        x = head
        while x:
            node_list.append(x)
            x = x.next

        i, j = 0, len(node_list)
        while i < j:
            node_list[i].next = node_list[j]
            i += 1
            if i < j:
                node_list[j].next = node_list[i]
            j -= 1
        node_list[i].next = None

        return


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    s.reorderList(head)
