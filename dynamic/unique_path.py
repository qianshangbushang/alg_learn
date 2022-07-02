#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :unique_path.py
# @Time      :2022/7/2 9:17


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        只能向下或者向右移动一步
        dp = [0] * n
        dp[0] = 1
        dp[i] = dp[i - 1] + dp[i]
        :param m:
        :param n:
        :return:
        """
        if m == 0 and n == 0:
            return 0

        if m == 1 or n == 1:
            return 1

        dp = [0] * n
        dp[0] = 1
        for _ in range(m):
            for i in range(1, n):
                dp[i] = dp[i] + dp[i - 1]
        return dp[-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        """
        只能向下或者向右移动一步
        dp[i,j] 表示移动到i,j的路径数
        dp[i,j] = dp[i, j -1] + dp[i-1, j]
        :param m:
        :param n:
        :return:
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            dp[x][0] = 1
        for x in range(n):
            dp[0][x] = 1
        print(dp)

        for idx in range(1, m):
            for idy in range(1, n):
                dp[idx][idy] = dp[idx][idy - 1] + dp[idx - 1][idy]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
