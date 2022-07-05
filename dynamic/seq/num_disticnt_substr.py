#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :num_disticnt_substr.py
# @Time      :2022/7/5 15:14


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """

        :param t:
        :param s:
        :return:
        """
        t_len = len(t)
        result = 0
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] == t_len:
                        result += 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))
