#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chenfama.py
# @Time      :2022/7/15 12:49


import sys


def run():
    sys.stdin.readline()
    m_list = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    x_list = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    print(logic(m_list, x_list))
    return


def logic2(m_list, x_list):
    item_list = m_list.copy()
    for i, m in enumerate(m_list):
        item_list.extend([m * j for j in range(2, x_list[i] + 1)])

    result = {0}
    for item in item_list:
        for elem in list(result):
            result.add(item + elem)
    print(len(result))
    # for j in range(2, x_list[i] + 1):
    #     item.ap


def logic(m_list, x_list):
    """
     dp[i] =max(dp[i - m] + m, dp[i]),能装的最大重量
    """
    total = sum([m_list[idx] * x_list[idx] for idx in range(len(m_list))])
    dp = [0] * (total + 1)

    for i, m in enumerate(m_list):
        w = total
        while w >= m:
            for j in range(1, x_list[i] + 1):
                if w - j * m < 0:
                    break
                dp[w] = max(dp[w], dp[w - j * m] + j * m)
            w -= 1
    # print(dp)
    result = 0
    for idx in range(len(dp)):
        if idx == dp[idx]:
            result += 1
    return result


run()
