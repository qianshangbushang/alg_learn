#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reverse_list_ii.py
# @Time      :2022/7/13 10:26


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        reverse_len = right - left + 1
        curr_node = dummy
        while left - 1 > 0:
            curr_node = curr_node.next
            left -= 1

        pre_node = curr_node
        curr_node = pre_node.next

        while reverse_len > 0:
            next_node = curr_node.next
            curr_node.next = next_node.next
            pre_node.next = next_node
            next_node.next = curr_node
            pre_node = pre_node.next
            reverse_len -= 1
        return dummy.next
