#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rotate_right.py
# @Time      :2022/10/27 17:01


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        pre, cnt = head, 1
        while pre.next:
            pre = pre.next
            cnt += 1

        k = k % cnt
        if k == 0:
            return head
        pre.next = head
        while k > 1:
            pre = pre.next
            k -= 1
        head = pre.next
        pre.next = None
        return head
