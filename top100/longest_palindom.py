#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :longest_palindom.py
# @Time      :2022/7/9 14:40


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        dp[i][j] 表示i开始j结束是否回文
        dp[i][j] = dp[i + 1][j - 1]
        :param s:
        :return:
        """

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        result = s[0]
        idx = len(s) - 1
        while idx >= 0:
            dp[idx][idx] = True
            for idy in range(idx + 1, len(s)):
                if s[idx] == s[idy]:
                    if idy - idx == 1:
                        dp[idx][idy] = True
                    else:
                        dp[idx][idy] = dp[idx + 1][idy - 1]
                if dp[idx][idy] and idy + 1 - idx > len(result):
                    result = s[idx:idy + 1]
            idx -= 1
        return result

    def longestPalindrome1(self, s: str) -> str:
        """
        输入：s = "babad"
        输出："bab"
        解释："aba" 同样是符合题意的答案。
        :param s:
        :return:
        """
        max_len = 1
        result = s[0]
        for idx in range(len(s)):
            for idy in range(idx, len(s)):
                if self.is_palindrome(s, idx, idy) and idy - idx + 1 > max_len:
                    result = s[idx:idy + 1]
                    max_len = idy + 1 - idx
        return result

    def is_palindrome(self, s: str, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome("1231", 1, 1))
    print(s.longestPalindrome("cbbd"))
