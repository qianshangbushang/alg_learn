#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :stock.py
# @Time      :2022/7/4 11:00


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        a: 当前如果持有：最大现金
        b: 当前不持有： 最大现金

        dp[i][0]: 第i天不持有的最大
        dp[i][1]: 第i天持有的最大
        a:  当前持有的最大
        b: 当前不持有的最大
        :param prices:
        :return:
        """
        a, b = -prices[0], 0
        for p in prices[1:]:
            a = max(a, p)
            b = max(a + p, b)
        return max(a, b)

        # dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        # dp[0][1] = -prices[0]

        # for idx in range(1, len(prices)):
        #     dp[idx][1] = max(dp[idx - 1][1], - prices[idx])
        #     dp[idx][0] = max(dp[idx - 1][1] + prices[idx], dp[idx - 1][0])
        #     print(dp)
        # return max(dp[len(prices) - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
