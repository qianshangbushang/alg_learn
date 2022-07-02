#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :max_profit.py
# @Time      :2022/7/1 22:57


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        result = 0
        for p in prices:
            if p < min_price:
                min_price = p
                continue

            if p > min_price + fee:
                result += p - (min_price + fee)
                min_price = p - fee
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 8, 4, 9], 2))
