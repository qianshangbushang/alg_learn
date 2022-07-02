#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :last_stone_weight.py
# @Time      :2022/7/2 19:34


from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        距离一半的最近一堆石头，造成最后剩下的重量最小

        target = sum(stones) // 2
        dp[i]: 重量为i的背包可装的最大石头重量
        dp[i] = max(dp[i], dp[i - stones[i]] + stones[i])
        :param stones:
        :return:
        """

        target = sum(stones) // 2
        dp = [0] * (target + 1)
        for x in stones:
            y = target
            while y >= x:
                dp[y] = max(dp[y], dp[y - x] + x)
                y -= 1
        return sum(stones) - 2 * dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
