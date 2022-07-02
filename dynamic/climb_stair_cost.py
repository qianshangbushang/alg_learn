#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :climb_stair_cost.py
# @Time      :2022/7/2 9:02


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i] 到第i阶的最小花费
        dp[0] = 0
        dp[1] = 0
        dp[2] = cost[i]
        dp[3] = min(dp[2] + cost[2], dp[1] + cost[1])

        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        :param cost:
        :return:
        """

        dp = [0] * (len(cost) + 1)

        dp[0] = 0
        dp[1] = 0
        a, b = 0, 0
        for idx in range(2, len(cost) + 1):
            # dp[idx] = min(dp[idx - 2] + cost[idx - 2], dp[idx - 1] + cost[idx - 1])
            a, b = b, min(a + cost[idx - 2], b + cost[idx - 1])
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
