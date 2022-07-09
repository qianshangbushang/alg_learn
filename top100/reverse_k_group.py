#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reverse_k_group.py
# @Time      :2022/7/9 1:05


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        dummy = ListNode(-1, head)
        prev_node, curr_node = dummy, head
        for i in range(length // k):
            for j in range(k - 1):
                next_node = curr_node.next
                curr_node.next = next_node.next
                next_node.next = prev_node.next
                prev_node.next = next_node
            prev_node = curr_node
            curr_node = curr_node.next
        return dummy.next
