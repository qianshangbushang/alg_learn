#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p1873.py
# @Time      :2022/10/31 9:10


from typing import List


def run():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    print(logic(data, m))
    return


# 大于等于target的最小
def logic(data: List[int], target: int):
    data.sort()
    # print(data)
    low, high = 0, max(data)
    while low < high:
        mid_h = low + (high + 1 - low) // 2
        sidx = find_idx(data, mid_h)
        recv = sum([x - mid_h for x in data[sidx:]])
        print(low, high, sidx, data[sidx:])
        if recv < target:
            high = mid_h - 1
        else:
            low = mid_h
    return low


# 大于等于target的最小的index
def find_idx(data: List[int], target):
    left, right = 0, len(data) - 1
    while left <= right:
        print(left, right)
        mid = left + (right - left) // 2
        if data[mid] == target:
            right = mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# run()
if __name__ == '__main__':
    # print(find_idx([1, 2, 3, 4, 5], 3))
    # print(find_idx([1, 2, 4, 5], 2))
    run()
