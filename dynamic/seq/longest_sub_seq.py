#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :longest_sub_seq.py
# @Time      :2022/7/5 18:15


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        https://leetcode.cn/problems/longest-palindromic-subsequence/
        dp[i][j]  i 与 j之间的回文子序列最大长度
        1. s[i] != s[j], dp[i][j] = dp[i][j-1]
        2. s[i] == s[j], dp[i][j] = dp[i-1][j-1] + 2
        :param s:
        :return:
        """

        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            dp[i][i] = 1

        for i in range(1, len(s) + 1):
            j = i - 1
            while j >= 1:
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i - 1][j])
                j -= 1
        print(*dp, sep='\n')
        return dp[-1][1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))
