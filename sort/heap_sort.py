#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :heap_sort.py
# @Time      :2022/8/12 13:36


from typing import List


def sort_array(nums: List[int]):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        sort(nums, i, n - 1)
    for i in range(n - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        sort(nums, 0, i - 1)
    return nums


def sort(nums: List[int], i, end):
    j = 2 * i + 1
    while j <= end:
        if j + 1 < end and nums[j] < nums[j + 1]:
            j = j + 1
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = 2 * j + 1
        else:
            break
    return


if __name__ == '__main__':
    print(sort_array([9, 6, 8, 2, 5, 1]))
