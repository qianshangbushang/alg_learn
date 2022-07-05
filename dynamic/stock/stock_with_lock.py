#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock_with_lock.py
# @Time      :2022/7/4 15:03


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        a:  买入
        b:  卖出
        c:  冷冻

        :param prices:
        :return:
        """
        a, b, c = -prices[0], 0, 0
        for idx in range(1, len(prices)):
            a, b, c = max(a, c - prices[idx]), max(b, a + prices[idx]), max(c, b)
        return max(b, c)

    def maxProfit1(self, prices: List[int]) -> int:
        """
        1. 买入
        2. 卖出未冷冻
        4. 冷冻
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        for idx in range(1, len(prices)):
            dp[idx][0] = max(dp[idx - 1][0], dp[idx - 1][2] - prices[idx])
            dp[idx][1] = max(dp[idx - 1][1], dp[idx - 1][0] + prices[idx])
            dp[idx][2] = max(dp[idx - 1][2], dp[idx - 1][1])
        print(dp)
        return max(dp[len(prices) - 1][1:])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
