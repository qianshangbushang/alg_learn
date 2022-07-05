#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :is_sub_seq.py
# @Time      :2022/7/5 15:03


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        dp[i][j] = dp[i-1][j-1] + 1
        :param s:
        :param t:
        :return:
        """
        s_len = len(s)
        if len(s) == 0:
            return True

        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i][j] == s_len:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("", "aafafa"))
