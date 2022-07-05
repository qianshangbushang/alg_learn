#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock_with_fee.py
# @Time      :2022/7/4 15:24


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        a  买入时的最大现金
        b  卖出时最大现金
        :param prices:
        :param fee:
        :return:
        """

        a, b = -prices[0], 0
        for p in prices:
            a = max(a, b - p)
            b = max(b, a + p - fee)
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
