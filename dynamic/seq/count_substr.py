#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :count_substr.py
# @Time      :2022/7/5 18:05


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        https://leetcode.cn/problems/palindromic-substrings/
        1. dp[i][j] = False
        2. i - j<= 1, dp[i][j] = True
        3, j - j > 1, dp[i][j] = dp[i -1][j-1]
        :param s:
        :return:
        """
        cnt = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(0, i + 1):
                if s[i] != s[j]:
                    dp[i][j] = False
                    continue

                if i - j <= 1:
                    dp[i][j] = True
                if i - j > 1:
                    dp[i][j] = dp[i - 1][j + 1]

                if dp[i][j]:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abc"))
    print(s.countSubstrings("aaa"))
