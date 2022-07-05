#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :min_distence.py
# @Time      :2022/7/5 16:31


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]: 以i-1结尾的word1和以j结尾的word2变相同需要的最小操作数
        :param word1:
        :param word2:
        :return:
        """

        max_val = len(word1) + len(word2)
        dp = [[max_val for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(0, len(word1) + 1):
            dp[i][0] = i
        for j in range(0, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("leetcode", "etco"))
