#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reverse_list.py
# @Time      :2022/7/9 2:45

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)

        curr_node, prev_node = head, dummy
        while curr_node.next:
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = prev_node.next
            prev_node.next = next_node
        return dummy.next
