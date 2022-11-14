#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p2240.py
# @Time      :2022/10/25 15:51


def run():
    n, t = map(int, input().split())
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().split())))
    print(f"{logic(lines, t):.2f}")
    return


def logic(data, total: int):
    data.sort(key=lambda x: x[1] / x[0], reverse=True)
    sum, idx = 0, 0
    while total > 0 and idx < len(data):
        if total > data[idx][0]:
            total -= data[idx][0]
            sum += data[idx][1]
            idx += 1
            continue
        sum += data[idx][1] * total / data[idx][0]
        break
    return sum


if __name__ == '__main__':
    run()
