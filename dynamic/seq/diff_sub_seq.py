#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :diff_sub_seq.py
# @Time      :2022/7/5 17:05


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i][j] 表示以i结尾的s中包含以j结尾的t的数量
        匹配上
        dp[i][j] = dp[i - 1][j - 1] + dp[i-1][j]
        未匹配上
        dp[i][j] = dp[i -1][j]
        :param s:
        :param t:
        :return:
        """

        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(*dp, sep='\n')
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))
    print(s.numDistinct("babgbag", "bag"))
    print(s.numDistinct("dd", "d"))
