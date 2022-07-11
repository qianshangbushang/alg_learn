#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :intersection_of_linklist.py
# @Time      :2022/7/11 14:29


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def count_link_list(self, node: ListNode):
        cnt = 0
        while node:
            node = node.next
            cnt += 1
        return cnt

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = self.count_link_list(headA)
        length_b = self.count_link_list(headB)

        if length_a - length_b > 0:
            n = length_a - length_b
            while n > 0:
                headA = headA.next
                n -= 1
        else:
            n = length_b - length_a
            while n > 0:
                headB = headB.next
                n -= 1

        while headA and headB:
            if headA == headB:
                return headB
            headA = headA.next
            headB = headB.next

        return None
