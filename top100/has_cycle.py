#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :has_cycle.py
# @Time      :2022/7/9 10:37


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            slow = slow.next

            if slow == fast:
                return True
        return False
