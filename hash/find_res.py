#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :find_res.py
# @Time      :2022/7/12 22:18


from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cnt_dict = {val: idx for idx, val in enumerate(list1)}
        result = []
        min_idx = 2000
        for idx2, val in enumerate(list2):
            if val not in cnt_dict:
                continue

            idx1 = cnt_dict[val]
            if idx1 + idx2 < min_idx:
                min_idx = idx1 + idx2
                result = [val]

            if idx1 + idx2 < min_idx:
                result.append(val)

        return result
