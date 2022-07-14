#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reorder_list.py
# @Time      :2022/7/14 10:31


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = []

        node = head
        while node:
            node_list.append(node)
            node = node.next

        dummy = ListNode(-1)
        pre = dummy

        left, right = 0, len(node_list) - 1
        while left < right:
            pre.next = node_list[left]
            pre = pre.next
            pre.next = None

            left += 1
            if left < right:
                pre.next = node_list[right]
                pre = pre.next
                pre.next = None
            right -= 1
        return dummy.next
