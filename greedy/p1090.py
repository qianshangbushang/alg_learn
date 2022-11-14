#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p1090.py
# @Time      :2022/10/25 16:14
from typing import List


def run():
    n = int(input())
    data = list(map(int, input().split()))
    print(logic(data, n))


def logic(data1: List[int], n):
    data1.sort(key=lambda x: x)
    data2 = [float('inf') for _ in data1]
    cnt, i, j, m, ret = 0, 0, 0, 0, 0
    while cnt < n - 1:
        if i < len(data1) and data1[i] < data2[j]:
            a1 = data1[i]
            i += 1
        else:
            a1 = data2[j]
            j += 1

        if i < len(data1) and data1[i] < data2[j]:
            a2 = data1[i]
            i += 1
        else:
            a2 = data2[j]
            j += 1

        ret += (a1 + a2)
        data2[m] = a1 + a2
        m += 1
        cnt += 1
    return ret


if __name__ == '__main__':
    run()
