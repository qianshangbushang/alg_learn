#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sort.py
# @Time      :2022/8/16 10:23


from typing import List


def sort_array(nums: List[int]):
    quick_sort(nums, 0, len(nums) - 1)
    return


def heap_sort(nums: List[int]):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        update_heap(nums, i, n)

    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        update_heap(nums, 0, i)
    return


def update_heap(nums: List[int], i: int, end: int):
    j = 2 * i + 1
    while j < end:
        if j + 1 < end and nums[j] > nums[j + 1]:
            j += 1
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = 2 * j + 1
        else:
            break
    return


def quick_sort(nums: List[int], i: int, j: int):
    left, right = i, j
    if left >= right:
        return

    mid = left + (right - left) // 2
    nums[mid], nums[right] = nums[right], nums[mid]
    flag = nums[right]
    while left < right:
        while nums[left] < flag and left < right:
            left += 1
        nums[right] = nums[left]

        while nums[right] >= flag and left < right:
            right -= 1
        nums[left] = nums[right]
    nums[left] = flag

    quick_sort(nums, i, left - 1)
    quick_sort(nums, left + 1, j)
    return


if __name__ == '__main__':
    arr = [3, 4, 2, 1, 6, 7, 5]
    # sort_array(arr)
    heap_sort(arr)
    print(arr)
