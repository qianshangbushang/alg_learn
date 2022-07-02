#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :coin_change.py
# @Time      :2022/7/2 21:44


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i]: 和为i的最少硬币个数

        dp[i] = min(dp, dp[i - coin] + 1)
        :param coins:
        :param amount:
        :return:
        """
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        for coin in coins:
            y = coin
            while y <= amount:
                dp[y] = min(dp[y], dp[y - coin] + 1)
                y += 1
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2147483647], 2))
