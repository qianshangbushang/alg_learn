#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :merge_list.py
# @Time      :2022/7/9 10:04


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pre = dummy
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                pre = list1
                list1 = list1.next

            pre.next = list2
            pre = list2
            list2 = list2.next
        pre.next = list1 if list1 else list2
        return dummy.next

