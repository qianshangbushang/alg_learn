#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock.py
# @Time      :2022/7/9 10:24


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        for p in prices[1:]:
            if p < buy:
                buy = p
            result = max(result, p - buy)
        return result
