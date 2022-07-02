#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :interger_break.py
# @Time      :2022/7/2 10:11


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        dp[i] i拆分后的最大乘积
        dp[i] = max(dp[i-1] * 1, dp[i-2] * 2, dp[i-3] *3 ....)
        dp[1] = 1
        dp[2] = 1
        dp[3] = max(dp[2] * 1, dp[1] * 2) = 2
        :param n:
        :return:
        """

        dp = [0] * (n + 1)

        dp[1], dp[2] = 1, 1

        for idx in range(3, n + 1):
            # tmp = []
            # for y in range(1, idx):
            #     tmp.append(max(y, dp[y]) * max(dp[idx - y], idx - y))
            # print(idx, tmp)
            # dp[idx] = max(tmp)
            dp[idx] = max([y * max(dp[idx - y], idx - y) for y in range(1, idx)])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))
    print(s.integerBreak(3))
