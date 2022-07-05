#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lcs.py
# @Time      :2022/7/5 14:09


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        if text1[i-1] == text2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        :param text1:
        :param text2:
        :return:
        """

        dp = [[0 for _ in range(len(text2) + 1)]for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))
