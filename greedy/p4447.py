#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p4447.py
# @Time      :2022/10/26 10:20


def run():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort(key=lambda x: x)

    lst_arr, len_arr = [], []
    for x in data:
        # 不存在连续的情况
        if x - 1 not in lst_arr:
            lst_arr.append(x)
            len_arr.append(1)
            continue
        # 存在连续的情况 可能有多个
        best_lst_idx = None
        best_lst_len = None
        for lst_idx in range(len(lst_arr)):
            if lst_arr[lst_idx] == x - 1:
                if not best_lst_len or best_lst_len > len_arr[lst_idx]:
                    best_lst_idx = lst_idx
                    best_lst_len = len_arr[lst_idx]
                    continue
        lst_arr[best_lst_idx] = x
        len_arr[best_lst_idx] += 1
    print(min(len_arr))


if __name__ == '__main__':
    run()
