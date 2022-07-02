#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :climb_stair.py
# @Time      :2022/7/2 8:51


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[i] = dp[i-1] + dp[i-2]
        dp[1] = 1, dp[2] = 2
        """
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
