#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :remove_nth_node.py
# @Time      :2022/7/14 11:01


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        return


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy

        while n >= 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

