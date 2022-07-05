#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock_iii.py
# @Time      :2022/7/4 12:09


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        a:  第一次买入最大收益
        b:  第一次卖出最大收益
        c:  第二次买入最大收益
        d:  第二次卖出最大收益

        第一次购买盈利大于当前价格，当天才有可能被作为买入点
        :param prices:
        :return:
        """
        dp = [[0 for _ in range(4)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for idx in range(1, len(prices)):
            dp[idx][0] = max(dp[idx - 1][0], -prices[idx])
            dp[idx][1] = max(dp[idx - 1][0] + prices[idx], dp[idx - 1][1])
            dp[idx][2] = max(dp[idx - 1][1] - prices[idx], dp[idx - 1][2])
            dp[idx][3] = max(dp[idx - 1][2] + prices[idx], dp[idx - 1][3])
        return dp[len(dp) - 1][3]


if __name__ == '__main__':
    s = Solution()
    # print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5, 1, 6]))
