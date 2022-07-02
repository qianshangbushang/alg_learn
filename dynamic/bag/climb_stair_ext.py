#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :climb_stair_ext.py
# @Time      :2022/7/2 21:34


class Solution(object):
    def climbStair(self, n: int, m: int):
        """
        dp[i] += dp[i - x]
        :param n:
        :return:
        """

        dp = [0] * (n + 1)
        dp[0] = 1
        for x in range(1, n + 1):
            for y in range(m):
                if x < y:
                    continue
                dp[x] = dp[x] + dp[x - y]

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStair(10, 3))
