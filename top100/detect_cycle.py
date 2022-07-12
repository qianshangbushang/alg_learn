#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :detect_cycle.py
# @Time      :2022/7/12 11:10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        环形链表，快慢指针
        :param head:
        :return:
        """
        slow, fast = head, head
        first = True
        while fast and (slow != fast or first):
            first = False
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
        if not fast:
            return None
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        return ptr
