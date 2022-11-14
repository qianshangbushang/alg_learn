#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p5019.py
# @Time      :2022/10/26 11:26


def run():
    n = int(input())
    data = list(map(int, input().split()))
    sum = data[0]
    for idx in range(1, len(data)):
        if data[idx] > data[idx - 1]:
            sum += data[idx] - data[idx - 1]
    print(sum)
    return


if __name__ == '__main__':
    run()
