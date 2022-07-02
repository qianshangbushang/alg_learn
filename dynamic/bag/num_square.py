#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :num_square.py
# @Time      :2022/7/2 22:16


class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[i]  构成i的最小完全平方数数量

        dp[i] = min(dp[i], dp[i - x**2] + 1)
        :param n:
        :return:
        """

        dp = [n] * (n + 1)
        dp[0] = 0

        nums = []
        i = 1
        i_square = i * i
        while i_square < n:
            nums.append(i_square)
            i += 1
            i_square = i * i

        for idx in range(1, n + 1):
            for x_square in nums:
                if x_square > idx:
                    break
                dp[idx] = min(dp[idx], dp[idx - x_square] + 1)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
