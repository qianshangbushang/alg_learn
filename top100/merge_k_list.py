#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :merge_k_list.py
# @Time      :2022/7/11 14:50


from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pre = dummy

        while len(lists) > 0:
            best_idx = -1
            for idx in range(len(lists)):
                if not lists[idx]:
                    continue

                if not pre.next or pre.next.val > lists[idx].val:
                    pre.next = lists[idx]
                    best_idx = idx

            if best_idx == -1:
                break
            lists[best_idx] = lists[best_idx].next
            pre = pre.next
        return dummy.next
