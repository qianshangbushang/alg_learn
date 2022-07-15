#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :hechangdui.py
# @Time      :2022/7/15 10:12


from typing import List
from collections import defaultdict

import sys
from typing import List


def remove_person(heights: List[int]):
    """
    ldp[i] 以i结束的最长递增序列长度
    rdp[i] 以i开始的最长递减序列长度
    """
    ldp, rdp = [1] * len(heights), [1] * len(heights)

    for idx in range(1, len(heights)):
        for idd in range(idx):
            if heights[idd] < heights[idx]:
                ldp[idx] = max(ldp[idx], ldp[idd] + 1)

    for idx in range(len(heights) - 1, -1, -1):
        for idd in range(len(heights) - 1, idx, -1):
            if heights[idx] > heights[idd]:
                rdp[idx] = max(rdp[idx], rdp[idd] + 1)

    max_best = ldp[0] + rdp[0] - 1
    for idx in range(len(heights)):
        max_best = max(ldp[idx] + rdp[idx] - 1, max_best)

    return len(heights) - max_best


def run():
    sys.stdin.readline()
    heights = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    print(remove_person(heights))
    return


run()

