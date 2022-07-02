#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :unique_path_ii.py
# @Time      :2022/7/2 9:45


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for idx in range(m):
            for idy in range(1, n):
                if obstacleGrid[idx][idy] == 1:
                    dp[idy] = 0
                    continue

                dp[idy] = dp[idy - 1] + dp[idy]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
