#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :min_distance_2.py
# @Time      :2022/7/5 16:51


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        1. dp[i][j] = dp[i-1][j-1]
        2. dp[i][j] = (dp[i-1][j], dp[j][i-1], dp[i-1][j-1]) + 1
        :param word1:
        :param word2:
        :return:
        """

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        # print(*dp, sep='\n')
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("intention", "execution"))
    print(s.minDistance("horse", "ros"))
