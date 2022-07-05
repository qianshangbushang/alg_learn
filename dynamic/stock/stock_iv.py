#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock_iv.py
# @Time      :2022/7/4 14:46


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """

        :param k:
        :param prices:
        :return:
        """

        dp = [[0 for _ in range(k * 2)] for _ in range(len(prices))]

        for i in range(0, 2 * k, 2):
            dp[0][i] = -prices[0]

        for idx in range(1, len(prices)):
            dp[idx][0] = max(dp[idx - 1][0], -prices[idx])
            dp[idx][1] = max(dp[idx - 1][1], dp[idx - 1][0] + prices[idx])

            for idy in range(1, k):
                dp[idx][2 * idy] = max(dp[idx - 1][2 * idy], dp[idx - 1][2 * idy - 1] - prices[idx])
                dp[idx][2 * idy + 1] = max(dp[idx - 1][2 * idy + 1], dp[idx - 1][2 * idy] + prices[idx])
        print(dp)
        return dp[len(prices) - 1][2 * k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(2, [2, 4, 1]))
