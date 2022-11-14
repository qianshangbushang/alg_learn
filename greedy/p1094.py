#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p1094.py
# @Time      :2022/10/26 11:10


def run():
    maxv = int(input())
    n = int(int(input()))
    data = [int(input()) for _ in range(n)]
    data.sort(key=lambda x: x)
    i, j, cnt = 0, len(data) - 1, 0

    while i <= j:
        if i == j:
            i += 1
            cnt += 1
            continue

        if data[i] + data[j] > maxv:
            j -= 1
        else:
            i += 1
            j -= 1
        cnt += 1
    print(cnt)
    return


if __name__ == '__main__':
    run()
